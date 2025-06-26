import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Define the function to interpolate
def f(x):
    return 1.0 / (1.0 + 25 * x**2)

# Generate 21 equally spaced points and evaluate the function at these points
N = 21
xin = np.linspace(-1, 1, N)
yin = f(xin)

# Define the linear interpolation using scipy
linear_interp = interp1d(xin, yin, kind='linear')

# Generate a dense set of x-values for plotting the interpolation
x_dense = np.linspace(-1, 1, 400)
y_actual = f(x_dense)
y_linear = linear_interp(x_dense)

# Plot the actual function and the interpolated data
plt.plot(xin, yin, 'o', label='Input data')
plt.plot(x_dense, y_linear, '-', label='Linear Interpolated data')
plt.plot(x_dense, y_actual, '--', label='Actual function')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Linear Interpolation')
plt.legend()
plt.show()
