import cv2
import numpy as np
from matplotlib import pyplot as plt
from ImageToArray import Image2Array
from blockshaped import blockshaped
array=np.random.randint(5, size=(8, 8))

Augmented = blockshaped(array, 2, 2)
print(Augmented)

size = Augmented.shape
print(Augmented[1])
print(np.mean(Augmented[1]))
print(type(Augmented))
print(len(Augmented))
print(size)
counter = 0
AverageMatrix = np.empty((4,4))
for i in range(0,4):
	for j in range(0,4):
		AverageMatrix[i][j] = np.mean(Augmented[counter])
		print(Augmented[counter])
		counter += 1

print(type(AverageMatrix))
print(AverageMatrix)
val=np.round(AverageMatrix,5)
print(val)

'a8','b8','c8','d8','e8','f8','g8','h8';
        'a7','b7','c7','d7','e7','f7','g7','h7';
        'a6','b6','c6','d6','e6','f6','g6','h6';
        'a5','b5','c5','d5','e5','f5','g5','h5';
        'a4','b4','c4','d4','e4','f4','g4','h4';
        'a3','b3','c3','d3','e3','f3','g3','h3';
        'a2','b2','c2','d2','e2','f2','g2','h2';
        'a1','b1','c1','d1','e1','f1','g1','h1';