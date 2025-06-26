from pylab import *

def legendrepol (x,beg,finish):          # poly interpolation at x 
    y = 0.                               # using input points from beg to finish
    for  i in range(beg,finish+1): 
       lambd = 1.0;
       for j in range(beg,finish+1):
           if i != j:                       #Lagrange polynom formed here
              lambd = lambd * ((x - xin[j])/(xin[i] - xin[j]))
       y += yin[i] * lambd
    return y

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

xvalues = range(0, 200, 1)  # Extended range up to 220 with a step of 1 for smoothness
yvalues = []

numpoints = m # use all points for interpolation
firstpoint = 0 # first point to use for interpolation

for x in xvalues:         
    yvalues.append(legendrepol(x, firstpoint, firstpoint + numpoints - 1))

plot(xin[0:m], yin[0:m], "o", label="input data")
plot(xvalues, yvalues, "-", label="Interpolated data")
xlabel('Energy (MeV')
ylabel('Cross Section (mb)')
title('Interpolation Methods')
legend(loc="upper right")
show()
