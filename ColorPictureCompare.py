#!/usr/bin/env python3
import cv2
import numpy as np
from blockshaped import blockshaped

def ColorPictureCompare(MovedFromIndex):
    counter = 0
    AverageMatrix = np.empty((8,8))
    AverageMatrix2 = np.empty((8,8))
    FinalMatrix = np.empty((8,8))

    img = cv2.imread(r'/home/pi/Prog/chess1_color.jpg')
    img  = cv2.resize(img,(400,400))
    img  = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    matrix = np.array(img)

    img2 = cv2.imread(r'/home/pi/Prog/chess2_color.jpg')
    img2  = cv2.resize(img2,(400,400))
    img2  = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
    matrix2 = np.array(img2)

    AugmentedMatrix = blockshaped(matrix, 50,50)
    for i in range(7,-1,-1):
            for j in range(7,-1,-1):
                AverageMatrix[i,j] = np.mean(AugmentedMatrix[counter])
                counter += 1

    counter = 0
    AugmentedMatrix2 = blockshaped(matrix2, 50,50)
    for i in range(7,-1,-1):
            for j in range(7,-1,-1):
                AverageMatrix2[i,j] = np.mean(AugmentedMatrix2[counter])
                counter += 1

    FinalMatrix = abs(AverageMatrix-AverageMatrix2)

    Value = [[0] * 2 for i in range(2)]
    for i in range(0,8):
        for j in range(0,8):
            if(FinalMatrix[i][j]>Value[0][0]):
                    if(Value[0][0]>Value[1][0]):
                        Value[1]=Value[0]
                    Value[0]=[FinalMatrix[i][j],i,j]
            elif(FinalMatrix[i][j]>Value[1][0]):
                Value[1]=[FinalMatrix[i][j],i,j]

    MovedToIndex = [[0] * 2 for i in range(2)]
    if(Value[0][1]==MovedFromIndex[0][0] and Value[0][2]==MovedFromIndex[1][0]):
            MovedToIndex[0][0] = Value[1][1]
            MovedToIndex[1][0] = Value[1][2]
    else:
        MovedToIndex[0][0] = Value[0][1]
        MovedToIndex[1][0] = Value[0][2]
    return MovedToIndex