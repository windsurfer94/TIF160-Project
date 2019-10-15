#!/usr/bin/env python3

def isCapturing(MainMatrixSecond,position,LANposition):
    for i in range(0,8):
        for j in range(0,8):
            if(LANposition[i][j]==position and MainMatrixSecond[i][j]=="1"):
                return 1
    return 0