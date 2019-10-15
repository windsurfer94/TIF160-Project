#!/usr/bin/env python3
#Import Libraries
import time
import chess
import chess.engine
import cv2
from matplotlib import pyplot as plt
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

#Import functions
from InitialChecks import InitialChecker #This should be completed ----
from CValgorithm import   CValgorithm
from CoordinateToLAN import CoordinateToLAN
from TakePictureCam import TakePictureCam
from isCapturing import isCapturing

#Initialize the chessboard
board = chess.Board()
print(board)

GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#Initizalize cheesboard for matrix operations

LANposition = (('a8','b8','c8','d8','e8','f8','g8','h8'),
                    ('a7','b7','c7','d7','e7','f7','g7','h7'),
                    ('a6','b6','c6','d6','e6','f6','g6','h6'),
                    ('a5','b5','c5','d5','e5','f5','g5','h5'),
                    ('a4','b4','c4','d4','e4','f4','g4','h4'),
                    ('a3','b3','c3','d3','e3','f3','g3','h3'),
                    ('a2','b2','c2','d2','e2','f2','g2','h2'),
                    ('a1','b1','c1','d1','e1','f1','g1','h1'))

#Initialize Chess Engine
engine = chess.engine.SimpleEngine.popen_uci(r"stockfish")
engine.id.get("name")

#Initizalize parameters
RobotCounter = 0
HumanCounter = 0
k=0
i=0

while not board.is_game_over():
    if GPIO.input(10) == GPIO.HIGH:
        TakePictureCam("chess1_color")
        img = cv2.imread(r'/home/pi/Prog/chess1_color.jpg') #this will be changed by webcam image
        MainMatrixInit,Av1 = CValgorithm(img) #here image will be changed with webcam image
        print(MainMatrixInit)
        while GPIO.input(10) != GPIO.HIGH:
            pass
        TakePictureCam("chess2_color")
        img2 = cv2.imread(r'/home/pi/Prog/chess2_color.jpg') #this will be changed by webcam image
        MainMatrixSecond,Av2 = CValgorithm(img2) #here image will be changed with webcam image
        print(MainMatrixSecond)
        MoveString = CoordinateToLAN(MainMatrixInit,MainMatrixSecond,Av1, Av2, LANposition) #detects the move in LAN (Algebraic Notation in Chess)

        HumanMove = chess.Move.from_uci(MoveString)
        board.push(HumanMove)
        HumanCounter += 1 #Count After Human Move
        print(board)
        print('////////////\n\n')

        limit = chess.engine.Limit(time=2.0)
        result =engine.play(board, limit)  # doctest: +ELLIPSIS
        print(board)
        board.push(result.move)
        new_pos = str(result.move)[2:3] #Return 0 if no piece is caught and 1 if a piece is caught
        print(isCapturing(MainMatrixSecond,new_pos, LANposition))
        print(result.move)
        print('////////////')
        print(board)

        RobotCounter += 1 #Count After Robot Move