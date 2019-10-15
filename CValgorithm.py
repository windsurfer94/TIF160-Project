#!/usr/bin/env python3

import cv2
import numpy as np
from matplotlib import pyplot as plt
from ImageToArray import Image2Array
#This part includes computer vision part where the chess layout is detected.

def CValgorithm(img):
    threshold = 0.09 #threshold value when deciding pieces on the chessboard
    dim = img.shape
    canny_param1, canny_param2=30,50;
    img  = cv2.resize(img,(400,400))
    img  = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    edged = cv2.Canny(img, canny_param1, canny_param2) #Canny method for edge detection
    cv2.imshow('ImageWindow', edged)
    cv2.waitKey()
    matrix = np.array(edged)
    MainMatrix,AverageMatrix = Image2Array(matrix,threshold) #Returned averaged matrix
    return MainMatrix,AverageMatrix