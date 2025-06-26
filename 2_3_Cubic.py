from scipy.interpolate import interp1d
import numpy as np
import matplotlib.pyplot as plt

# Function to perform cubic interpolation
def cubic_interpolate(x, y, x_new):
    cubic_interp = interp1d(x, y, kind='cubic', bounds_error=False, fill_value="extrapolate")
    return cubic_interp(x_new)

# Reading data from the file
NMAX = 100
xin = np.zeros(NMAX)
yin = np.zeros(NMAX)

with open("lagrange.dat", "r") as inputfile:
    lines = inputfile.readlines()

m = 0
for line in lines:
    s = line.split() 
    xin[m] = float(s[0])
    yin[m] = float(s[1])
    m += 1

# Trimming arrays to the actual number of points read
xin = xin[:m]
yin = yin[:m]

# Generating new x values for interpolation
x_new = np.linspace(min(xin), max(xin), 400)

# Performing cubic interpolation
y_new = cubic_interpolate(xin, yin, x_new)

# Plotting the results
plt.plot(xin, yin, "o", label="Input data")
plt.plot(x_new, y_new, "-", label="Cubic Interpolated data")
plt.xlabel('Energy (MeV)')  # Corrected
plt.ylabel('Cross Section (mb)')  # Corrected
plt.title('Interpolation Methods')  # Corrected
plt.legend(loc="upper right")
plt.show()

