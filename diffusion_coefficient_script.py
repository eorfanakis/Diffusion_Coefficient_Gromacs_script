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
slope = coeff[0]
intercept = coeff[1]

# R-squared
residuals = msd - (slope * time + intercept)
ssr = np.sum(residuals**2)
sst = np.sum((msd - np.mean(msd))**2)
r_squared = 1 - (ssr / sst)

# Convert time units left and right tau limits
left_tau_limit = min(time) / 1000  # Conversion from ps to ns
right_tau_limit = max(time) / 1000  # Conversion from ps to ns

# Standard error
std_err = np.sqrt(ssr / (len(time) - 2))

# Diffusion Coefficient value
diffusion_coeff = slope / 6.0

print('Left Tau Limit: {:.3f} ns'.format(left_tau_limit))
print('Right Tau Limit: {:.3f} ns'.format(right_tau_limit))
print('Standard Error: {:.6f} m^2/s'.format(std_err))
print('Slope: {:.6f} A^2/ns'.format(slope))
print('Y-intercept: {:.6f} A^2'.format(intercept))
print('R-squared: {:.6f}'.format(r_squared))
print('Diffusion Coefficient: {:.6f} nm^2/ps'.format(diffusion_coeff))
