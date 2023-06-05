# Face Mask Detection on Real-World Webcam Images
<p align="left""><b>Authors:</b><br/>Eashan Adhikarla<br/>Dr. Brian D. Davison</p>
Paper: https://doi.org/10.1145/3462203.3475903

The COVID-19 pandemic has been one of the biggest health crises in recent memory. According to leading scientists, face masks and maintaining six feet of social distancing are the most substantial protections to limit the virus’s spread. Experimental data on face mask usage in the US is limited and has not been studied in scale. Thus, an understanding of population compliance with mask recommendations may be helpful in current and future pandemic situations. Knowledge of mask usage will help researchers answer many questions about the spread in various regions. One way to understand mask usage is by monitoring human behavior through publicly available webcams. Recently, researchers have come up with abundant research on face mask detection and recognition but their experiments are performed on datasets that do not reflect real-world complexity. In this paper, we propose a new webcam based real-world face-mask detection dataset of over 1TB of images collected across different regions of the United States, and we implement state-of-the-art object detection algorithms to understand their effectiveness in such a real-world application. <p><br/></p>

- Face Detection and Mask Detection on Times Square, New York
<p align="center">
  <img width="500" height="500" src="https://github.com/eashanadhikarla/wfm/blob/main/sample/title_fig.jpeg">
</p>

- Mask Detection on (a.)Cats and Meows Karaoke Bar, New Orleans, LA, (b.) Bourbon Street, New Orleans, (c.) Church Street Market Place, Burlington, VT (d.) Times Square, New York <p><br/></p>
<p align="center">
  <img width="500" height="450" src="https://github.com/eashanadhikarla/wfm/blob/main/sample/main.png">
</p>

## Dataset (download the annoted images below)
Dropbox link: https://www.dropbox.com/sh/peymbuh9yidww61/AAC2YHDkDIp_W_qSnXE_7vQPa?dl=0

### Characteristics of a good dataset
1) Significant real-world diversity (e.g., of location, time of day, distance to subjects, and number of subjects);
2) Authentic masked images (as opposed to artificial masks over prior images); and, 
3) Annotations that are compatible with many existing models. 
Our dataset generally reflects these goals.

## Training on YOLOv5-TTA
~~~
git clone https://github.com/eashanadhikarla/wfm
cd yolov5
conda env create --file=environment.yaml
# arrange the dataset in the manner as shown in the tree below
python train.py --img 640 --batch 16 --epochs 3 --data webcam.yaml --weights yolov5s.pt
~~~

## Directory tree
```
yolo-v5/
│
├── train.py
├── test.py
├── data/
│  ├── webcam.yaml
├── weights/
│  ├── yolov5-tta.pt
├──dataset
│  ├── images/
│  │   ├── train/
│  │   │   ├── train-image-1.png
│  │   │   ├── train-image-2.png
│  │   │   ├── ...
│  │   ├── val/
│  │   │   ├── val-image-1.png
│  │   │   ├── val-image-2.png
│  │   │   ├── ...
│  ├── labels/
│  │   ├── train/
│  │   │   ├── train-image-1.txt
│  │   │   ├── train-image-2.txt
│  │   │   ├── ...
│  │   ├── val/
│  │   │   ├── val-image-1.txt
│  │   │   ├── val-image-2.txt
│  │   │   ├── ...
│  │   │
│  │
│
```

## Experiments

| Model | Size<br>(Pixels) | Model<br>Size(mb) | Inference<br>time (ms) | Precision<br>(P) | Recall<br>(R) | AP<br>(mask) | AP<br>(no-mask) |  AP<br>(unsure) | mAP<sup>test<br>@0.5 |
|---               |---  |---    |---     |---      |---      |---      |---      |---      |---
| YOLOv3<sup>tiny  |640  |17.4   |**5.4** |21.4     |25.2     |17.7     |23.3     |3.94     |14.9
| YOLOv3           |640  |123.4  |13.8    |27.5     |36.6     |35.2     |36.0     |8.44     |26.8
| Faster-RCNN      |600  |329.7  |54.24   |27.7     |39.2     |34.8     |38.6     |10.9     |28.1
| YOLOv3<sup>SPP   |640  |125.5  |13.2    |27.9     |38.7     |35.7     |37       |10.7     |27.8
| RetinaNet        |800  |155    |24.8    |32.2     |35.2     |36.9     |39.8     |10.1     |29
| Mask-RCNN        |600  |176.3  |237.8   |33.1     |36.8     |39.7     |42.2     |11.3     |31
| YOLOv5x          |640  |171.1  |36.1    |36.1     |33.5     |37.1     |40.2     |10.3     |29.2
| YOLOv5x          |1280 |1055   |35.7    |32.6     |37.7     |41.8     |46.7     |**11.7** |33.8
| YOLOv5x6<sup>TTA |1280 |1130   |39.2    |**37.0** |**41.6** |**46.5** |**47.4** |11.2     |**35.1**

## Citation
If you use this repo or find it useful, please consider citing:
```
@inproceedings{10.1145/3462203.3475903,
author = {Adhikarla, Eashan and Davison, Brian D.},
title = {Face Mask Detection on Real-World Webcam Images},
year = {2021},
isbn = {9781450384780},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
url = {https://doi.org/10.1145/3462203.3475903},
doi = {10.1145/3462203.3475903},
abstract = {The COVID-19 pandemic has been one of the biggest health crises in recent memory.
According to leading scientists, face masks and maintaining six feet of social distancing
are the most substantial protections to limit the virus's spread. Experimental data
on face mask usage in the US is limited and has not been studied in scale. Thus, an
understanding of population compliance with mask recommendations may be helpful in
current and future pandemic situations. Knowledge of mask usage will help researchers
answer many questions about the spread in various regions. One way to understand mask
usage is by monitoring human behavior through publicly available webcams. Recently,
researchers have come up with abundant research on face mask detection and recognition
but their experiments are performed on datasets that do not reflect real-world complexity.
In this paper, we propose a new webcam-based real-world face-mask detection dataset
of over 1TB of images collected across different regions of the United States, and
we implement state-of-the-art object detection algorithms to understand their effectiveness
in such a real-world application.},
booktitle = {Proceedings of the Conference on Information Technology for Social Good},
pages = {139–144},
numpages = {6},
keywords = {Webcam Images, Face-Mask Detection, COVID-19, Real-World Dataset},
location = {Roma, Italy},
series = {GoodIT '21}
}
```
                                                                                                      ![Visitor Count](https://profile-counter.glitch.me/{username}/count.svg)

