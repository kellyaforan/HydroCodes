""" 
Writing Hydro Codes: Finite Differencing (FTCS vs Lax-Friedrich)
Advection Equation

Author: Kelly Foran
November 12, 2020
"""


#importing the necessary packages
import matplotlib.pyplot as plt
import numpy as np
import time

#Setting up grid spacing, time step spacing and velocity
dx = 10
dt = 10
u = -0.1

#Setting up number of grid points and time steps
Nx = 50
Nt = 500

#Finding the constant term, setting up the x array, finding the initial state for each function
#f1 is for FTCS method and f2 is for Lax-Friedrich method
k = u*dt/(2*dx)
x = np.arange(0, Nx*dx, dx)
f1 = x/Nx
f2 = x/Nx

#Setting up a figure with two panels to compare FTCS and Lax-Friedrich side-by-side
#This portion is from an example given in class by Eve Lee (I am not experienced with setting up multiple plots in one figure)
plt.ion()
figure, ax = plt.subplots(1,2)
ax[0].plot(x, f1, 'k--')
ax[1].plot(x, f2, 'k--')
pl1, = ax[0].plot(x, f1, 'b.')
pl2, = ax[1].plot(x, f2, 'b.')
ax[0].set_xlim([0,Nx*dx])
ax[0].set_ylim([0,2*dx])
ax[0].set_title('FTCS')
ax[0].set_xlabel('Position, x')
ax[0].set_ylabel('Fluid Quantity, f')
ax[1].set_xlim([0,Nx*dx])
ax[1].set_ylim([0,2*dx])
ax[1].set_title('Lax-Friedrich')
ax[1].set_xlabel('Position, x')
figure.canvas.draw()

#Calculating and plotting f1, f2 through time using the FTCS method (f1) and the Lax-Friedrich method (f2)
for t in range(0, Nt):
    for j in range(1,Nx-1):
        f1[j] = f1[j] - k*(f1[j+1] - f1[j-1])
        f2[j] = 0.5*(f2[j+1]+f2[j-1]) - k*(f2[j+1] - f2[j-1])
    pl1.set_ydata(f1)
    pl2.set_ydata(f2)
    figure.canvas.draw()
    time.sleep(0.001)
