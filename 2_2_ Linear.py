
from pylab import *

from pylab import *

def linear_interpolate(x0, y0, x1, y1, x):
    return y0 + (y1 - y0) * (x - x0) / (x1 - x0)

NMAX = 100  # max number of input points

xin = zeros(NMAX)  # each is array of length NMAX, all elements set to zero
yin = zeros(NMAX)

inputfile = open("lagrange.dat","r")  # read in the input x,y values
r = inputfile.readlines()  # read the whole file into list (one item per line)
inputfile.close()
        # input has the form: x0 y0
        #                     x1 y1
        #                     ...

m = 0
for line in r:
    #print(line)
    s = line.split() # split line and split into list of items(assume items separated by spaces)
    xin[m] = s[0] # first number in each line is the x value
    yin[m] = s[1]
    print(xin[m],yin[m])
    m+=1         # m is total number of input data points
                 # will be stored in xin[0]..xin[m-1],yin[0].yin[m-1]
xvalues = range(0, 201, 1)  # x-values between 0 and 200
yvalues = []

numpoints = m # use all points for interpolation
firstpoint = 0 # first point to use for interpolation

for x in xvalues:
    # Find the two nearest points
    for i in range(m - 1):
        if xin[i] <= x <= xin[i + 1]:
            yvalues.append(linear_interpolate(xin[i], yin[i], xin[i + 1], yin[i + 1], x))
            break

plot(xin[0:m], yin[0:m], "o", label="input data")
plot(xvalues, yvalues, "-", label="Linear Interpolated Data")
plt.xlabel('Energy (MeV)')  # Corrected
plt.ylabel('Cross Section (mb)')  # Corrected
plt.title('Interpolation Methods')  # Corrected
legend(loc="upper right")
show()
