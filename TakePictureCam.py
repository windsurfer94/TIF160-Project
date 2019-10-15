#!/usr/bin/env python3
import cv2
import sys
import numpy as np

from PIL import Image

def TakePictureCam(name):
    capture = cv2.VideoCapture("/dev/video0")
    # Check success
    if not capture.isOpened():
        raise Exception("Could not open video device")
    # Read picture. ret === True on success
    ret, img = capture.read()
    # Close device
    capture.release()
    x, xend, y, yend = 118, 455, 68,405;
    crop_img=img[y:yend,x:xend]
    cv2.imwrite("/home/pi/Prog/"+name+".jpg",crop_img)