"""
Detect person object on the video, given an Youtube video URL.
Generate a video that shows and track the existence of humans
within the video by drawing boxes around them for each frame.
For different humans, different colors must be used.

# Requirements:
Env with Python 3.7.6 or later (I use Python 3.7.13)

# Install required packages
pip install -r requirements.txt

# Run
python3 aive-detection.py --url https://www.youtube.com/watch?v=h4s0llOpKrU

"""

import aive
import os
import argparse
import sys
from imageai.Detection import ObjectDetection
# import random
# from itertools import product

# Use 'argparse' to get youtube url
parser = argparse.ArgumentParser(description="Download youtube video from url")
parser.add_argument("--url", help="youtube url to download")
args = parser.parse_args()  # parses sys.argv

# Youtube url, i.e. marketing video of Dior commercial
# VIDEO_URL = "https://www.youtube.com/watch?v=h4s0llOpKrU"

# Directory to save the downloaded video
VIDEO_IN_PATH = 'video_in'

# Directory to save video frame
VIDEO_OUT_PATH = 'video_out'

# Directory to save the audi file
AUDIO_PATH = 'audio'

# Audio fime name
AUDIO_NAME = 'dior_audio'

# Audio fime extension
AUDIO_EXT = '.mp3'

# Detection model path
MODEL_PATH = 'models/resnet50_coco_best_v2.1.0.h5'  # RetinaNet
# MODEL_PATH = 'models/yolo.h5' # Yolo Net
# MODEL_PATH = 'models/yolo-tiny.h5' # Yolo Tiny Net

# Output video name WITHOUT audio
OUT_VIDEO_NAME = 'dior_box_NO_music'

# Output video name WITH audio
OUT_VIDEO_MUSIC_NAME = 'dior_box_music'

# Output video extension '.mp4' or '.avi'
OUT_VIDEO_EXT = '.mp4'

# Color list
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 0, 255), (0, 255, 255), (255, 50, 0), (50, 255, 0), (50, 0, 255)]

# ----- Other method to generate Color list at scale -----
# rgb_pixel = list(range(0,255,50))
# random.shuffle(rgb_pixel)
# COLORS = list(product(rgb_pixel,rgb_pixel,rgb_pixel))
# random.shuffle(COLORS)

# Get current directory of the python file
execution_path = os.getcwd()

# load detector from ObjectDetection class
detector = ObjectDetection()

# Set ReninaNet for video detection
detector.setModelTypeAsRetinaNet()

# Load RetinaNet model
detector.setModelPath(os.path.join(execution_path, MODEL_PATH))
detector.loadModel()

# Customize Object: Only detect 'person' object
custom_objects = detector.CustomObjects(person=True)


def main(url_path):
    """
    Get a youtube video url, this function make person detection on each frame, then generate the processed video.
    Different person has different bounding box color. The audio is combined with the processed video at the end
    of the pileline
    :param url_path: Youtube video url
    :return: processed video with object detection, combined with its original audio
    """
    # ------------- Create Directory & Path - -------------  #
    # Create download directory for video
    aive.create_dir(VIDEO_IN_PATH)

    # Create directory for extracted audio
    aive.create_dir(AUDIO_PATH)

    # Create output video directory to save processed video
    aive.create_dir(VIDEO_OUT_PATH)

    # Get audio path
    audio_path = os.path.join(AUDIO_PATH, AUDIO_NAME + AUDIO_EXT)

    # Get path of video output without music
    output_video_no_ext = os.path.join(VIDEO_OUT_PATH, OUT_VIDEO_NAME)
    output_video_path = os.path.join(VIDEO_OUT_PATH, OUT_VIDEO_NAME + OUT_VIDEO_EXT)

    # Create path of the final processed video with its original music
    combined_output_video = os.path.join(VIDEO_OUT_PATH, OUT_VIDEO_MUSIC_NAME + OUT_VIDEO_EXT)

    # ------------- Download Video, Extract Audio, Object Detection & Render --------------#

    # Download youtube video and get video path
    video_path = aive.download_youtube_video(url_path, VIDEO_IN_PATH)

    # Extract audio from video and show audio path
    aive.extract_audio_from_video(video_path, audio_path)

    # Run the model prediction for video object detection
    aive.render_video_detection(video_path, output_video_no_ext, detector, custom_objects, COLORS, ext=OUT_VIDEO_EXT)

    # Start render final video with music and saving
    _ = aive.render_video_music(output_video_path, audio_path, combined_output_video)


if __name__ == '__main__':
    url = args.url

    if url is None:
        print('----------IMPORTANT----------')
        print("Give me an Youtube URL please!", file=sys.stderr)
        print('----------IMPORTANT----------')
        sys.exit(-1)
    else:
        main(url)
