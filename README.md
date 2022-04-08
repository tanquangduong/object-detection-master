# aive-object-detection-master
This repository is used for detect person object on the video, given an Youtube video URL. Generate a video that shows and track the existence of humans within the video by drawing boxes around them for each frame. For different humans, different colors must be used.

# Object detection package
I use the ImageAI package to make custom object detection on each frame. Please refer the following repo for detailed information
https://github.com/OlafenwaMoses/ImageAI/blob/master/imageai/Detection/README.md

# IMPORTANT - Download model first
Please download the models and put it in the 'models' folder of this repository

- [RetinaNet](https://1drv.ms/u/s!ApH9RKcWDsubhdMuX9KVrJTHSEj0_A?e=GHBFvX) (Size = 145 mb, high performance and accuracy, with longer detection time)

- [YOLOv3](https://1drv.ms/u/s!ApH9RKcWDsubhdMvc4HD6z0Py6bE7Q?e=p27Dkt) (Size = 237 mb, moderate performance and accuracy, with a moderate detection time)

- [TinyYOLOv3](https://1drv.ms/u/s!ApH9RKcWDsubhdMtrrPjWJG3pYHLBA?e=eHtwMW) (Size = 34 mb, optimized for speed and moderate performance, with fast detection time)

# Download My result

- [Result-Tan-Quang](https://1drv.ms/u/s!ApH9RKcWDsubhdM4MVuene0bPqw9_w?e=6aflFD) (Input Video, Output Videos, Audio)
