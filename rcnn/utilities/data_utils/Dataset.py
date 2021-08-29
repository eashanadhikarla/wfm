import torch
import os
from PIL import Image
from xml.dom.minidom import parse
import numpy as np
import utilities.transforms as T

class FacialDataset(object):
    def __init__(self, root, transforms, train=True):
        self.root = root
        self.transforms = transforms
        # load all image files, sorting them to
        # ensure that they are aligned
        self.train = train
        self.imgs = list(sorted(os.listdir(os.path.join(root, "images"))))
        self.annotations = list(sorted(os.listdir(os.path.join(root, "annotations"))))

    def __getitem__(self, idx):
        # load images
        img_path = os.path.join(self.root+"/images", self.imgs[idx])
        img = Image.open(img_path).convert("RGB")

        annotation_path = os.path.join(self.root+"/annotations", self.annotations[idx])

        dom = parse(annotation_path)
        root = dom.documentElement
        objects = root.getElementsByTagName("object")
        size = root.getElementsByTagName("size")[0]

        image_width = int(size.getElementsByTagName("width")[0].childNodes[0].data)
        image_height = int(size.getElementsByTagName("height")[0].childNodes[0].data)

        masks = np.zeros((len(objects), image_width, image_height))
        boxes = []
        labels = []
        box_num = 0

        for box in objects:

            cls_name = box.getElementsByTagName("name")[0].childNodes[0].data
            xmin = int(float(box.getElementsByTagName("xmin")[0].childNodes[0].data))
            ymin = int(float(box.getElementsByTagName("ymin")[0].childNodes[0].data))
            xmax = int(float(box.getElementsByTagName("xmax")[0].childNodes[0].data))
            ymax = int(float(box.getElementsByTagName("ymax")[0].childNodes[0].data))

            boxes.append([xmin, ymin, xmax, ymax])

            if cls_name in ["with_mask", "with-mask", "0"]:
                labels.append(0)
            elif cls_name in ["without_mask", "without-mask", "1"]:
                labels.append(1)
            elif cls_name in ["mask_weared_incorrect", "unsure", "2"]:
                labels.append(2)

            for i in range(xmin, min(xmax+1, image_width)):
                for j in range(ymin, min(ymax+1, image_height)):
                    masks[box_num, i, j] = 1
            box_num += 1

        # convert everything into a torch.Tensor
        boxes = torch.as_tensor(boxes, dtype=torch.float32)
        labels = torch.as_tensor(labels, dtype=torch.int64)
        masks = torch.as_tensor(masks, dtype=torch.uint8)
        image_id = torch.tensor([idx])
        area = torch.as_tensor((boxes[:, 3] - boxes[:, 1]) * (boxes[:, 2] - boxes[:, 0]), dtype=torch.float32)
        # iscrowd is needed in evaluation, which converts everything into coco datatype
        iscrowd = torch.zeros((len(objects),), dtype=torch.int64)

        target = {}
        target["boxes"] = boxes
        target["labels"] = labels
        target["masks"] = masks
        target["image_id"] = image_id
        target["area"] = area
        target["iscrowd"] = iscrowd

        if self.transforms is not None:
            img, target = self.transforms(img, target)

        return img, target

    def __len__(self):
        return len(self.imgs)


def get_transform(horizontal_flip):
    transforms = []
    # converts the image, a PIL image, into a PyTorch Tensor
    transforms.append(T.ToTensor())

    if horizontal_flip:
        transforms.append(T.RandomHorizontalFlip(0.5))
    return T.Compose(transforms)
