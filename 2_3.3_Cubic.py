from scipy.interpolate import interp1d
import numpy as np
import matplotlib.pyplot as plt

# Linear interpolation function
def linear_interpolate(x0, y0, x1, y1, x):
    return y0 + (y1 - y0) * (x - x0) / (x1 - x0)

# Lagrange polynomial interpolation function
def legendrepol(x, xin, yin):
    y = 0.
    n = len(xin)
    for i in range(n):
        lambd = 1.0
        for j in range(n):
            if i != j:
                lambd *= (x - xin[j]) / (xin[i] - xin[j])
        y += yin[i] * lambd
    return y

# Cubic interpolation function
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

# Trimming arrays to the actual number of points
xin = xin[:m]
yin = yin[:m]

# Generating new x values for interpolation
x_new = np.linspace(min(xin), max(xin), 400)

# Linear Interpolation
y_linear = [linear_interpolate(xin[i], yin[i], xin[i + 1], yin[i + 1], x) for i in range(m - 1) for x in x_new if xin[i] <= x <= xin[i + 1]]

# Lagrange Polynomial Interpolation
y_lagrange = [legendrepol(x, xin, yin) for x in x_new]

# Cubic Interpolation
y_cubic = cubic_interpolate(xin, yin, x_new)

# Plotting the results
plt.plot(xin, yin, "o", label="Input data")
plt.plot(x_new, y_linear, "-", label="Linear Interpolated data")
plt.plot(x_new, y_lagrange, "-", label="Lagrange Interpolated data")
plt.plot(x_new, y_cubic, "-", label="Cubic Interpolated data")
plt.xlabel('Energy (MeV)')
plt.ylabel('Cross Section (mb)')
plt.title('Interpolation Methods')
plt.legend(loc="upper right")
plt.show()
