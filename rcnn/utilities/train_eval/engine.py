import math
import sys
import time
import torch
from PIL import Image, ImageDraw
import torchvision.models.detection.mask_rcnn

from utilities.coco_utils.coco_utils import get_coco_api_from_dataset
from utilities.coco_utils.coco_eval import CocoEvaluator
from utilities import utils
import numpy as np
import os

def train_one_epoch(model, optimizer, data_loader, device, epoch, print_freq):
    model.train()
    torch.set_num_threads(1)
    metric_logger = utils.MetricLogger(delimiter="  ")
    metric_logger.add_meter('lr', utils.SmoothedValue(window_size=1, fmt='{value:.5f}'))
    header = 'Epoch: [{}]'.format(epoch)

    lr_scheduler = None
    if epoch == 0:
        warmup_factor = 1. / 1000
        warmup_iters = min(1000, len(data_loader) - 1)

        lr_scheduler = utils.warmup_lr_scheduler(optimizer, warmup_iters, warmup_factor)

    for images, targets in metric_logger.log_every(data_loader, 1, header):
        images = list(image.to(device) for image in images)
        targets = [{k: v.to(device) for k, v in t.items()} for t in targets]

        loss_dict = model(images, targets)

        losses = sum(loss for loss in loss_dict.values())

        # reduce losses over all GPUs for logging purposes
        loss_dict_reduced = utils.reduce_dict(loss_dict)
        losses_reduced = sum(loss for loss in loss_dict_reduced.values())

        loss_value = losses_reduced.item()

        if not math.isfinite(loss_value):
            print("Loss is {}, stopping training".format(loss_value))
            print(loss_dict_reduced)
            sys.exit(1)

        optimizer.zero_grad()
        losses.backward()
        optimizer.step()

        if lr_scheduler is not None:
            lr_scheduler.step()

        metric_logger.update(loss=losses_reduced, **loss_dict_reduced)
        metric_logger.update(lr=optimizer.param_groups[0]["lr"])

    return metric_logger


def _get_iou_types(model):
    model_without_ddp = model
    if isinstance(model, torch.nn.parallel.DistributedDataParallel):
        model_without_ddp = model.module
    iou_types = ["bbox"]
    
    if isinstance(model_without_ddp, torchvision.models.detection.MaskRCNN):
        iou_types.append("segm")
    
    if isinstance(model_without_ddp, torchvision.models.detection.KeypointRCNN):
        iou_types.append("keypoints")
    return iou_types


@torch.no_grad()
def evaluate(model, data_loader, device):
    # n_threads = torch.get_num_threads()
    # print('n_threads = ', n_threads)
    # FIXME remove this and make paste_masks_in_image run on the GPU
    # torch.set_num_threads(1)
    cpu_device = torch.device("cpu")
    model.eval()
    
    metric_logger = utils.MetricLogger(delimiter="  ")
    header = 'Test:'

    coco = get_coco_api_from_dataset(data_loader.dataset)
    iou_types = _get_iou_types(model)
    coco_evaluator = CocoEvaluator(coco, iou_types)

    for images, targets in metric_logger.log_every(data_loader, 100, header):
        images = list(img.to(device) for img in images)
        targets = [{k: v.to(device) for k, v in t.items()} for t in targets]

        torch.cuda.synchronize()
        model_time = time.time()
        outputs = model(images)

        outputs = [{k: v.to(cpu_device) for k, v in t.items()} for t in outputs]
        model_time = time.time() - model_time

        res = {target["image_id"].item(): output for target, output in zip(targets, outputs)}
        evaluator_time = time.time()
        coco_evaluator.update(res)
        evaluator_time = time.time() - evaluator_time
        metric_logger.update(model_time=model_time, evaluator_time=evaluator_time)

    # gather the stats from all processes
    metric_logger.synchronize_between_processes()
    print("Averaged stats:", metric_logger)
    coco_evaluator.synchronize_between_processes()

    # accumulate predictions from all images
    coco_evaluator.accumulate()
    coco_evaluator.summarize()
    # torch.set_num_threads(n_threads)
    return coco_evaluator
       

@torch.no_grad()
def get_model_result(img, model, target, i, device, location="", conf_threshold=0.40, iou_threshold=0.40):
    model.eval()
    prediction = model([img.to(device)])
    prediction = prediction[0]
    boxes, scores, labels = prediction["boxes"], prediction["scores"], prediction["labels"]
    labels = labels.detach().cpu().numpy()
    text_labels = []
    
    for i in range(len(labels)):
        if labels[i]==0:
            text_labels.append("with mask")
        elif labels[i]==1:
            text_labels.append('without mask')
        elif labels[i]==2:
            text_labels.append('unsure')
        
    orig = Image.fromarray(img.mul(255).permute(1, 2, 0).byte().numpy())
    
    # In case no boxes are predicted by the model
    if boxes.size()==torch.Size([0, 4]):
        orig.save(os.path.join(location, "result" + str(i) + "_noboxes.png"))
        print("No prediction for", i)
        return
    
    # To choose boxes above threshold
    n_s = scores.cpu().numpy()
    ind = np.where(n_s>conf_threshold)
    ind = ind[0]
    
    # In case no boxes are above threshold
    if len(ind)==0:
        ind=[0]
        
    # Applying NMS
    boxes = boxes[ind]
    n_s = n_s[ind]
    # iou_threshold=0.45
    ind = torchvision.ops.nms(boxes.cpu(), torch.from_numpy(n_s), iou_threshold)
    
    for j in range(len(target['boxes'])):
        box = target['boxes'][j]
        box = box.tolist()
        draw = ImageDraw.Draw(orig)
        draw.text((box[0], box[1] - 10), "GT", fill=(255, 40, 40))
        draw.rectangle(box, outline="green")
        del draw
        
    for j in ind:
        box = boxes[j]
        box = box.tolist()
        draw = ImageDraw.Draw(orig)
        if labels[j] == 1:
            draw.text((box[0], box[1]-10), text_labels[j], fill=(40,40,255))
            draw.rectangle(box, outline = "blue")
        elif labels[j]==2:
            draw.text((box[0], box[1] - 10), text_labels[j], fill=(255, 40, 40))
            draw.rectangle(box, outline="red")
        del draw
    
    orig.save(os.path.join(location, "result" + str(i) + ".png"))
