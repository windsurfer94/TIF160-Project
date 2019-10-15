#!/usr/bin/env python3
import cv2
import numpy as np
from matplotlib import pyplot as plt

capture = cv2.VideoCapture("/dev/video2")
# Check success
if not capture.isOpened():
	raise Exception("Could not open video device")
# Read picture. ret === True on success
ret, img = capture.read()
# Close device
capture.release()
cv2.imwrite('/home/remi/Humanoid-Robotics/test.jpg',img)

img2 = cv2.imread('/home/remi/Humanoid-Robotics/test.jpg')
dim = img2.shape
img2 = cv2.resize(img2,(400,400))
img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
edged = cv2.Canny(img2, 25, 50)
cv2.imwrite('/home/remi/Humanoid-Robotics/chess.jpg',edged)

w, h = 400, 400;
matrix = [[0 for x in range(w)] for y in range(h)] 
for x in range(0,399):
	for y in range(0,399):
		matrix[x][y] = edged[x][y]

w, h, l, m, n = 400, 400, 8, 0, 0;
average = [[0 for o in range(l)] for p in range(l)]
for x in range(0,399):
	m=0
	for y in range(0,399):
		average[n][m]+=matrix[x][y]
		if(y%50==0 and y!= 0):
			m = m+1
	if(x!=0 and (x%50==0 or x==399)):
		n = n+1;

for x in range(0,8):
	for y in range (0,8):	
		average[x][y]/=400;
		if(average[x][y]<100):
			average[x][y]=0
		else:
			average[x][y]=1
		print(average[x][y], end = '')
	print()
