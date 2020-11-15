"""
Writing Hydro Codes: Finite Differencing
Advection-diffusion equation

Author: Kelly Foran
November 13, 2020
"""

#importing the necessary packages
import matplotlib.pyplot as plt
import numpy as np
import time

#Setting up grid spacing, time step spacing and velocity
dx = 1
dt = 1
u = -0.1

#Setting up number of grid points and time steps
Nx = 50
Nt = 500

#Finding the constant term for advection, setting up the x array, finding the initial state for each function
#f1 and f2 will have different diffusion co-efficients
k = u*dt/(2*dx)
x = np.arange(0, Nx*dx, dx)
f1 = x/Nx
f2 = x/Nx

#Setting the diffusion co-efficients and calculating the constant beta (called b here) for the implicit diffusion calculation
D1 = 0.2
D2 = 2.0
b1 = D1*dt/(dx**2)
b2 = D2*dt/(dx**2)

#Setting up a figure with two panels to compare two different diffusion co-efficients
#This portion is from an example given in class by Eve Lee (I am not experienced with setting up multiple plots in one figure)
plt.ion()
figure, ax = plt.subplots(1,2)
ax[0].plot(x, f1, 'k--')
ax[1].plot(x, f2, 'k--')
pl1, = ax[0].plot(x, f1, 'b.')
pl2, = ax[1].plot(x, f2, 'b.')
ax[0].set_xlim([0,Nx*dx])
ax[0].set_ylim([0,2*dx])
ax[0].set_title('D = %1.3f'%D1)
ax[1].set_xlim([0,Nx*dx])
ax[1].set_ylim([0,2*dx])
ax[1].set_title('D = %1.3f'%D2)
figure.canvas.draw()

#Setting up the matrix for the implicit operator splitting diffusion method 
#This setup was given in the Writing Hydro Codes handout
A1 = np.eye(Nx)*(1+2*b1) +np.eye(Nx, k=1)*-b1+np.eye(Nx, k=-1)*-b1
A2 = np.eye(Nx)*(1+2*b2) +np.eye(Nx, k=1)*-b2+np.eye(Nx, k=-1)*-b2

#Setting up the boundaries 
#Since we want both sides to be a fixed boundary the first and last diagonal terms are set to 1
#A no-slip fixed boundary also needs the first and last off-diagonal terms to be zero to ensure no diffusive flux through the boundary
A1[0][0] = 1
A1[0][1] = 0
A1[Nx-1][Nx-1] = 1
A1[Nx-1][Nx-2] = 0
A2[0][0]=1
A2[0][1]=0
A2[Nx-1][Nx-1] = 1
A2[Nx-1][Nx-2] = 0

#Calculating and plotting the progression of each function through time
#At each time, the diffusion term is calculated first and then the advection term
t = 0
while t < Nt*dt:
    f1 = np.linalg.solve(A1,f1)
    f2 = np.linalg.solve(A2,f2)
    for j in range(1, Nx-1):
        f1[j] = 0.5*(f1[j+1]+f1[j-1]) - k*(f1[j+1] - f1[j-1])
        f2[j] = 0.5*(f2[j+1]+f2[j-1]) - k*(f2[j+1] - f2[j-1])
    pl1.set_ydata(f1)
    pl2.set_ydata(f2)
    figure.canvas.draw()
    time.sleep(0.001)
    t = t+dt
