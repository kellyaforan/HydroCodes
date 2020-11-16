# HydroCodes

### Author Name: Kelly Foran

### Python Version: 3.x

### Files: 

  - *advection.py* : Produces a plot showing the time progression of a pure advection scenario using both the FTCS and LAx-Friedrich Finite Differencing methods

  - *advection-diffusion.py* : Produces a plot showing the time progression of the advection-diffusione equation for two different diffusion co-efficients (uses the Lax-Frierich method for calculating the advection term and the implicit method for calculating the diffusion term)

  - *hydrosolver.py* : Produces a plot of density (evolving over time) for a small perturbation in a 1-D medium. Calculations are done using the donor cell advection scheme. Note: a shock (sudden jump in density) can be seen. The width of the shock seems to be determined by the sound speed used. 
