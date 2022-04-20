# aive-object-detection-master
This repository is used for detecting human object on the video, given an Youtube video URL. Generate a video that shows and track the existence of humans within the video by drawing boxes around them for each frame. For different humans, different colors must be used.

# IMPORTANT - Download model first
Please download the models and put it in the 'models' folder of this repository

- [RetinaNet](https://1drv.ms/u/s!ApH9RKcWDsubhdMuX9KVrJTHSEj0_A?e=GHBFvX) (Size = 145 mb, high performance and accuracy, with longer detection time)

- [YOLOv3](https://1drv.ms/u/s!ApH9RKcWDsubhdMvc4HD6z0Py6bE7Q?e=p27Dkt) (Size = 237 mb, moderate performance and accuracy, with a moderate detection time)

- [TinyYOLOv3](https://1drv.ms/u/s!ApH9RKcWDsubhdMtrrPjWJG3pYHLBA?e=eHtwMW) (Size = 34 mb, optimized for speed and moderate performance, with fast detection time)

# Needed Package Versions

- pytube==12.0.0
- moviepy==1.0.3
- tensorflow==2.4.0
- tensorflow-gpu==2.4.0
- keras==2.4.3 
- numpy==1.19.3 
- pillow==7.0.0 
- scipy==1.4.1 
- h5py==2.10.0 
- matplotlib==3.3.2 
- opencv-python 
- keras-resnet==0.2.0
- imageai==2.1.6

# How to use:
## Step 1: Set up Python environment:
Env with Python 3.7.6 or later (I use 3.7.13)

## Step 2: Install required packages
pip install -r requirements.txt

## Step3: Run this line on terminal 
python3 aive-detection.py --url https://www.youtube.com/watch?v=h4s0llOpKrU

# Download Outputs

- [Output Videos](https://1drv.ms/u/s!ApH9RKcWDsubhdM5BirtQ0COGXDyxw?e=x8cqRV) 

# INPUT FOLDER STRUCTURE:
```bash
.
├── aive
│   ├── __pycache__
│   │   ├── __init__.cpython-37.pyc
│   │   └── utils.cpython-37.pyc
│   ├── __init__.py
│   └── utils.py
├── models
│   ├── resnet50_coco_best_v2.1.0.h5
│   ├── yolo.h5
│   └── yolo-tiny.h5
├── aive-detection.ipynb
├── aive-detection.py
├── requirements.txt
└── setup.py
```

# OUTPUT FOLDER STRUCTURE:
```bash
.
├── aive
│   ├── __pycache__
│   │   ├── __init__.cpython-37.pyc
│   │   └── utils.cpython-37.pyc
│   ├── __init__.py
│   └── utils.py
├── audio
│   └── dior_audio.mp3
├── models
│   ├── resnet50_coco_best_v2.1.0.h5
│   ├── yolo.h5
│   └── yolo-tiny.h5
├── video_in
│   └── MISS DIOR – The new Eau de Parfum.mp4
├── video_out
│   ├── dior_box_music.mp4
│   └── dior_box_NO_music.mp4
├── aive-detection.ipynb
├── aive-detection.py
├── requirements.txt
└── setup.py
```
