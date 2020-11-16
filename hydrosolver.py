"""
Writing Hydro Codes: 1-D Hydro Solver
Author: Kelly Foran
November 15, 2020
"""

#importing the necessary packages
import matplotlib.pyplot as plt
import numpy as np
import time

#Setting up grid spacing, time step spacing and sound speed
dx = 0.5
dt = 0.1
cs = 1

#Setting up number of grid points and time steps
Nx = 50
Nt = 200

#Setting up the x direction, density (f1) and density*speed (f2) with the correct number of points (same as grid spacing)
#Setting up the fluid speed (u) and flux (J1, J2) with one additional point since we look at boundaries
x = np.arange(0, Nx*dx, dx)
f1 = np.ones(Nx)/Nx
f2 = np.ones(Nx)/Nx
u = np.ones(Nx+1)/Nx
J1 = np.ones(Nx+1)/Nx
J2 = np.ones(Nx+1)/Nx

#Setting the reflective boundary conditions
f1[0] = f1[0] - (dt/dx)*J1[0]
f1[-1] = f1[-1] + (dt/dx)*J1[-2]
f2[0] = f2[0] - (dt/dx)*J2[0]
f2[-1] = f2[-1] + (dt/dx)*J2[-2]

#Setting up the figure to plot density 
plt.ion()
figure = plt.figure()
pl1, = plt.plot(x, f1, 'b-')
plt.ylim([-10,10])
plt.xlabel('Position, x')
plt.ylabel('Density')
plt.title('Density along a 1-D Medium')
figure.canvas.draw()

#Calculating and plotting the density (f1) at each timestep 
for t in range(0,Nt):
    for j in range(1, Nx-1):
        u[j] = 0.5*((f2[j]/f1[j])+(f2[j-1]/f1[j-1]))
        if u[j] > 0:
            J1[j] = u[j]*f1[j-1]
            J2[j] = u[j]*f2[j-1]
        if u[j] < 0:
            J1[j] = u[j]*f1[j]
            J2[j] = u[j]*f2[j]
        f1[j] = f1[j] - (dt/dx)*(J1[j+1] - J1[j])
        f2[j] = f2[j] - (dt/dx)*(J2[j+1] - J2[j]) - (dt/dx)*(cs**2)*(f1[j+1]-f1[j-1])
    pl1.set_ydata(f1)
    figure.canvas.draw()
    time.sleep(0.001)
