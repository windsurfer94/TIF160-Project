import cv2
import numpy as np
from matplotlib import pyplot as plt
from ColorPictureCompare import ColorPictureCompare

def CoordinateToLAN(MainMatrixInit,MainMatrixSecond,Av1, Av2, LANposition):

    BoardStatus = MainMatrixSecond-MainMatrixInit
    AvStatus = Av2-Av1
    MovedFromIndex = np.where(BoardStatus == -1) #index of the sqaure where the chess piece moved FROM
    MovedToIndex = np.where(BoardStatus == 1) #index of the sqaure where the chess piece moved TO
    print(MovedToIndex)
    if(not(np.any(MovedToIndex))):
        MovedToIndex = [[0] * 2 for i in range(2)]
        MovedToIndex = ColorPictureCompare(MovedFromIndex)
    MovedFrom = LANposition[MovedFromIndex[0][0]][MovedFromIndex[1][0]]
    MovedTo = LANposition[MovedToIndex[0][0]][MovedToIndex[1][0]]
    MoveString =  MovedFrom + MovedTo
    print(MovedFrom)
    print(MovedTo)
    return MoveString