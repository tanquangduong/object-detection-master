"""
This is setup file for aive package.
"""
from setuptools import setup
setup(name='aive',
      version='0.0.1',
      description='This is a computer vision package of AIVE. It is used for object detection or object segmentation.',
      author='Tan-Quang DUONG',
      author_email='tquangbk@gmail.com',
      packages=['aive'],
      install_requires=['pytube==12.0.0',
                        'moviepy==1.0.3',
                        'tensorflow==2.4.0',
                        'tensorflow-gpu==2.4.0',
                        'keras==2.4.3',
                        'numpy==1.19.3',
                        'pillow==7.0.0',
                        'scipy==1.4.1',
                        'h5py==2.10.0',
                        'matplotlib==3.3.2',
                        'opencv-python',
                        'keras-resnet==0.2.0',
                        'imageai==2.1.6'])
