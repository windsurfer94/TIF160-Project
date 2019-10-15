import numpy as np
from scipy.optimize import minimize, Bounds
#Desired position from chess engine(for robot)
from math import cos, sin, sqrt
import time

# do stuff

L1 = 0.055
L2 = 0.315
L3 = 0.045
L4 = 0.108
L5 = 0.005
L6 = 0.034
L7 = 0.015
L8 = 0.088
L9 = 0.204
xdes = 0.3 #This will be changed by input from the chess engine (x cordinates of desired position)
ydes = 0.155 #This will be changed by input from the chess engine (y cordinates of desired position)
zdes = 0.329 #This will be changed by input from the chess engine (z cordinates of desired position)

def objective(th):
    th1 = 0.01745*th[0]
    th2 = 0.01745*th[1]
    th3 = 0.01745*th[2]
    x = L6*cos(th1) + L4*sin(th1) - L5*sin(th1) + cos(th1)*(L7*cos(th2) + L8*sin(th2)) + L9*cos(th1)*cos(th2)*sin(th3) + L9*cos(th1)*cos(th3)*sin(th2) - 0.3
    y = L5*cos(th1) - L4*cos(th1) + L6*sin(th1) + sin(th1)*(L7*cos(th2) + L8*sin(th2)) + L9*cos(th2)*sin(th1)*sin(th3) + L9*cos(th3)*sin(th1)*sin(th2) - 0.155
    z = L2 + L3 - L8*cos(th2) + L7*sin(th2) - L9*cos(th2)*cos(th3) + L9*sin(th2)*sin(th3) - 0.329 
    e = sqrt(x*x + y*y + z*z)
    return e

num_iter = 50

th1_init = np.linspace(-80, 80, num=num_iter) #Number of initial conditions to iterate optimization can be decreased to minimize computation time on Rasperry Pi
th2_init = np.linspace(-80, 50, num=num_iter) #Number of initial conditions to iterate optimization can be decreased to minimize computation time on Rasperry Pi
th3_init = np.linspace(-80, 50, num=num_iter) #Number of initial conditions to iterate optimization can be decreased to minimize computation time on Rasperry Pi

x0 = np.vstack((th1_init, th2_init,th3_init))
#Initialize matrices for objective function solution and a corresponding angle values
Solutions = np.empty((num_iter,1))
OptimizedAngles = np.empty((num_iter,3))

t = time.time()                                                                
for i in range(0,num_iter):
    sol = minimize(objective, x0[:,i], bounds=Bounds([-70,0,-90],[70,90,0])) #optimization tool
    Solutions[i,0] = sol.fun #objective function value
    OptimizedAngles[i,:] = sol.x #angle values for corresponding o.f. value
elapsed = time.time() - t

Opt_Index = np.where(Solutions == np.min(Solutions))    #Index value for the angles which give the best optimized solution
Opt_Index = Opt_Index[0]
Opt_angle = OptimizedAngles[Opt_Index,:]
print('Joint angles: ' + str(Opt_angle[0]))
#print(Opt_Index)
print('Residual: ' + str(np.min(Solutions)))
print('Elapsed time: ' + str(elapsed))
#return Opt_angle