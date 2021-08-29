import os
import glob
from utilities.data_utils.Dataset import FacialDataset, get_transform
from utilities.utils import collate_fn
from utilities.train_eval.engine import train_one_epoch, evaluate, get_model_result

import torch
import torch.nn as nn
from torch.utils.data import DataLoader
import torchvision
from torchvision.models.detection.faster_rcnn import FastRCNNPredictor
from torchvision.models.detection.rpn import AnchorGenerator, RPNHead
import nvidia_smi # for python 3, you need nvidia-ml-py3 library

from torchvision.models.detection import FasterRCNN
from torchvision.models.detection.rpn import AnchorGenerator
from torchvision.models.detection.faster_rcnn import FastRCNNPredictor
from torchvision.models.detection.mask_rcnn import MaskRCNNPredictor


save_model_folder = 'model'
output_image_folder = 'output'
path = "./" # Put the absolute path instead

num_classes = 3 
batch_size = 16
num_epochs = 150

momentum = 0.9
learning_rate = 0.001
weight_decay = 0.0005

step_size = 5
gamma = 0.1


if __name__ == "__main__":
    
    device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
    torch.cuda.empty_cache()
    nvidia_smi.nvmlInit()
    handle = nvidia_smi.nvmlDeviceGetHandleByIndex(0)
    info = nvidia_smi.nvmlDeviceGetMemoryInfo(handle)

    print("Total memory:", info.total)
    print("Free memory:", info.free)
    print("Used memory:", info.used)

    traindata = FacialDataset(
        str(path)+'data/train',
        get_transform(horizontal_flip=True)
        )
    testdata  = FacialDataset(
        str(path)+'data/test',
        get_transform(horizontal_flip=False)
        )
    trainloader = DataLoader(
        traindata,
        batch_size=batch_size,
        shuffle=True,
        drop_last=True,
        collate_fn=collate_fn
        )
    testloader = DataLoader(
        testdata,
        batch_size=batch_size,
        shuffle=True,
        collate_fn=collate_fn
        )
    
    # load a pre-trained model for classification and return only the features
    backbone = torchvision.models.mobilenet_v2(pretrained=True).features
    
    # FasterRCNN needs to know the number of
    # output channels in a backbone. For mobilenet_v2, it's 1280
    # so we need to add it here
    backbone.out_channels = 1280

    # let's make the RPN generate 5 x 3 anchors per spatial
    # location, with 5 different sizes and 3 different aspect
    # ratios. We have a Tuple[Tuple[int]] because each feature
    # map could potentially have different sizes and
    # aspect ratios
    anchor_generator = AnchorGenerator(sizes=((32, 64, 128, 256, 512),), 
                                       aspect_ratios=((0.5, 1.0, 2.0),))

    # let's define what are the feature maps that we will
    # use to perform the region of interest cropping, as well as
    # the size of the crop after rescaling.
    # if your backbone returns a Tensor, featmap_names is expected to
    # be [0]. More generally, the backbone should return an
    # OrderedDict[Tensor], and in featmap_names you can choose which
    # feature maps to use.
    roi_pooler = torchvision.ops.MultiScaleRoIAlign(featmap_names=['0'], 
                                                    output_size=7, 
                                                    sampling_ratio=2)
    
    # put the pieces together inside a FasterRCNN model
    model = FasterRCNN(backbone, 
                       num_classes=3, 
                       rpn_anchor_generator=anchor_generator, 
                       box_roi_pool=roi_pooler)
    
    # load an instance segmentation model pre-trained pre-trained on COCO
    model = torchvision.models.detection.maskrcnn_resnet50_fpn(pretrained=True)
    
    # get number of input features for the classifier
    in_features = model.roi_heads.box_predictor.cls_score.in_features
    
    # replace the pre-trained head with a new one
    model.roi_heads.box_predictor = FastRCNNPredictor(in_features,
                                                      num_classes=3)
    
    # now get the number of input features for the mask classifier
    in_features_mask = model.roi_heads.mask_predictor.conv5_mask.in_channels
    hidden_layer = 256
    
    # and replace the mask predictor with a new one
    model.roi_heads.mask_predictor = MaskRCNNPredictor(in_features_mask, 
                                                       hidden_layer, 
                                                       num_classes=3)

    if torch.cuda.device_count() > 1:
        print("Use", torch.cuda.device_count(), "GPUs!")
        # model = nn.DataParallel(model)
    
    model.to(device)

    params = [p for p in model.parameters() if p.requires_grad]
    optimizer = torch.optim.SGD(params, lr=learning_rate, momentum=momentum, weight_decay=weight_decay)
    lr_scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=step_size, gamma=gamma)

    for epoch in range(num_epochs):
        res = nvidia_smi.nvmlDeviceGetUtilizationRates(handle)
        print(f'gpu: {res.gpu}%, gpu-mem: {res.memory}%')

        train_one_epoch(
            model,
            optimizer,
            trainloader,
            device,
            epoch,
            print_freq=10
            )
        lr_scheduler.step()
        evaluate(
            model,
            testloader,
            device=device
            )
        torch.save(
            model.state_dict(),
            os.path.join(save_model_folder, 'mrcnn_'+str(num_epochs)+'.pth')
            )

    print("Training complete!")
    
    # Create output directory
    if not os.path.exists(output_image_folder):
        os.mkdir(output_image_folder)
    else:
        files = glob.glob(output_image_folder + '/*')
        for f in files:
            os.remove(f)
    # write testing result to output folder
    for img_idx, batch_sampler in enumerate(testloader):
        img_test = batch_sampler[0][0]
        target_test = batch_sampler[1][0]
        i = target_test["image_id"].item()
        get_model_result(
            img_test,
            model,
            target_test,
            i,
            device,
            location=output_image_folder,
            conf_threshold=0.15,
            iou_threshold=0.45
            )

    print("Testing complete!")
    torch.cuda.synchronize()

    # Create directory for saving the model
    if not os.path.exists(save_model_folder):
        os.mkdir(save_model_folder)

    print("Saving model...")
    torch.save(
        model.state_dict(),
        os.path.join(save_model_folder, 'mrcnn_'+str(num_epochs)+'_last.pth')
        )

    print("Model saving complete!")
    nvidia_smi.nvmlShutdown()
    
#===============================================














