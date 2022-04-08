"""
This is the utils file of 'aive' package. It includes the following functions:
- create_dir
- download_youtube_video
- extract_audio_from_video
- draw_boxes
- render_video_detection
- render_video_music
"""
# Importing required libraies
import os
import pytube
import cv2 as cv
import time
from moviepy.editor import VideoFileClip, AudioFileClip


# Function to create a directory to save downloaded video
def create_dir(dir_name):
    """ Create a directory if not existed.

    :param dir_name: directory name

    :returns: A new created directory
    """
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)


# Download youtube video from url
def download_youtube_video(url, download_dir):
    """ Download youtube video from video url

    :param
        url_path: url path of the video
        download_dir: path to the download directory

    :returns:
        video_path: (str) path to the downloaded video
    """
    # Load Youtube url into pytube
    youtube = pytube.YouTube(url)

    # Set Streams resolution
    video = youtube.streams.get_highest_resolution()

    # Start downloading youtude video
    video.download(download_dir)

    # Get a list of video names
    video_files = os.listdir(download_dir)

    # Get video name
    video_name = video_files[0]

    # Get video path
    video_path = os.path.join(download_dir, video_name)

    # Print downloaded video path
    print('Video file is saved at: {}'.format(video_path))

    return video_path


# Extract audio from video
def extract_audio_from_video(video_file, audio_path):
    """ Extract audio from video using MoviePy library
    that uses `ffmpeg` under the hood

    :param
        video_file: path to the video file
        output_ext: audio output extension

    :returns: audio file is saved in the same folder of video file
    """
    # Get Clip file
    clip = VideoFileClip(video_file)

    # Save audio file
    clip.audio.write_audiofile(audio_path)

    print('Audio file is saved at: {}'.format(audio_path))


# Function to draw all detected boxes over the video frame
def draw_boxes(image, box_points, colors):
    """ Draw rectangle box for each object detection.
    Different detection has different box color.
    This function is generalized for as many as detected objects. The color
    list is now randomly choice in function of the number of detected object.

    :param
        image: video frame under ndarray

        box_points: A list of box coordinate tuples for each detection. Example: [(20,30,50,60),(15,35,40,65)]

    :returns image under ndarray
    """

    for i, box in enumerate(box_points):
        # It is ok now for the Dior video in term of box color, but if the video has a lot of people detection, then
        # 'colors' should be genereated at scale as many as object detection.
        if i <= len(colors) - 1:
            # Get coordinates of each box for each detection
            xmin, ymin, xmax, ymax = box

            # Draw box with OpenCV
            cv.rectangle(image, (xmin, ymin), (xmax, ymax), colors[i], 2)

    return image


def render_video_detection(video_path, output_path, detector, custom_objects, colors, ext='.mp4'):
    """ Make object detection on each frame extracted from the video.
    Render processed frames into the output video.
    Function actually supports only .mp4 and .avi as output extension. Default is .mp4

    :param
        video_path: Path to the input video
        output_path: Path to the output video without extension
        detector: detection model
        custom_objects: ex. only 'person'
        box_colors: a list of rgb color for each bounding box
        ext: video extension
    :returns video with detected objects on each frame

    """

    # Set starting time
    start_time = time.time()

    # Capture video with OpenCV
    input_video = cv.VideoCapture(video_path)

    # Get video FPS
    fps = input_video.get(cv.CAP_PROP_FPS)

    # Get frame width and frame height
    frame_width = int(input_video.get(3))
    frame_height = int(input_video.get(4))

    # Set parameter for video encoder, adapting to the desired video extension, i.e. '.mp4' or '.avi'
    if ext == '.avi':
        # Create output video path
        output_video_filepath = output_path + ext
        output_video = cv.VideoWriter(output_video_filepath,
                                      cv.VideoWriter_fourcc('M', 'J', 'P', 'G'),
                                      fps,
                                      (frame_width, frame_height)
                                      )
    else:  # .mp4
        # Create output video path
        output_video_filepath = output_path + '.mp4'
        output_video = cv.VideoWriter(output_video_filepath,
                                      cv.VideoWriter_fourcc(*'mp4v'),
                                      fps,
                                      (frame_width, frame_height)
                                      )

    # initialize video reading status
    success = True
    count = 0

    # read video from the first to the last frame
    while success:

        # read each frame, return status 'success' and video frame
        success, frame = input_video.read()

        # if there is still frame to read
        if success:
            # Model prediction: Detect only custom objects, i.e. person.
            _, detections = detector.detectCustomObjectsFromImage(custom_objects=custom_objects,
                                                                  input_image=frame,
                                                                  input_type="array",
                                                                  output_type="array",
                                                                  minimum_percentage_probability=50,
                                                                  display_percentage_probability=False,
                                                                  display_object_name=False)

            # Create a list of box coordinates of each detection
            box_points = [detection['box_points'] for detection in detections]

            # Draw the rectanges over each frame. Different box color for each person
            detected_frame_array = draw_boxes(frame, box_points, colors)

            # Write detected frame array into output video
            output_video.write(detected_frame_array)

            # Print # frame being processing
            count += 1
            print("Frame: {} is processed.".format(count))
            print('----------------------')

    # Finished. Release input and output video
    input_video.release()
    output_video.release()

    # Print finish status and the processing time
    print("Your processed video WITHOUT music is saved at: {}".format(output_video_filepath))
    print("Rendering Video-detection is finished in {} minutes.".format(round((time.time() - start_time) / 60, 2)))


def render_video_music(video_path, audio_path, combined_video_path):
    """ Render object-detected video with its original audio.

    :param
        video_path: Path to the processed video with object detection
        audio_path: Path to audio file
        combined_video_path: Path to save final video with audio
    :returns Final video with detected objects on each frame and its audio

    """

    # loading video dsa gfg intro video
    clip = VideoFileClip(video_path)

    # loading audio file
    audioclip = AudioFileClip(audio_path)

    # adding audio to the video clip
    videoclip = clip.set_audio(audioclip)

    # saving the final processed video with music
    videoclip.write_videofile(combined_video_path)
    # Print finish status and the processing time
    print("Your combined video with music is saved at: {}".format(combined_video_path))

    return videoclip
