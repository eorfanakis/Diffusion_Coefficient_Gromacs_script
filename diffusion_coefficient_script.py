import numpy as np
import matplotlib.pyplot as plt

# Load MSD data from the Gromacs output .xvg file
data = np.loadtxt('msd.xvg', skiprows=17)
time = data[:, 0]  # Time in ps
msd = data[:, 1]   # Mean square displacement in nm^2

# Change the axis titles as you like and then plot the MSD curve
plt.plot(time, msd)
plt.xlabel('Time (ps)')
plt.ylabel('Mean Square Displacement (nm^2)')
plt.title('Mean Square Displacement vs. Time')
plt.grid(True)
plt.show()

# Fit the curve to calculate diffusion coefficient 
coeff = np.polyfit(time, msd, 1)
diffusion_coeff = coeff[0] / 6.0
print('Diffusion Coefficient: {:.6f} nm^2/ps'.format(diffusion_coeff))
