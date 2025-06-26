# integ.py: trapezoid and Simpson integration, a<x<b, N pts, N-1 intervals 
from pylab import * # import numpy and matplotlib

def func(x):  # function to be integrated
    return sin(exp(5.0)*x+7.0)

def trapezoid(A,B,N):   #integrate from A to B using N points
    h = (B - A)/(N - 1)                     # step size 
    sum = (func(A)+func(B))/2               # (1st + last)/2
    for i in range(1, N-1):        # i goes from 1 to (N-1)-1
       sum += func(A+i*h)          # to simulate single-precision (32 bit) calculation
    return h*sum  

def simpson(A,B,N):
    if ((N-1)%2==1):     #  if number of intervals odd
        print("Simpson's rule requires even number of intervals")
        return 0
    h = (B - A)/(N - 1)                     # step size 
    sum = (func(A)+func(B))/3               # (1st + last)/3
    for i in range(1, N-1,2):        # i loops over odd integers  from 1 to (N-1)-1
       sum += 4/3*func(A+i*h)
    for i in range(2, N-1,2):        # i loops over even integers starting with 2
       sum += 2/3*func(A+i*h)
    return h*sum  

def Romberg_extrap(A,B,N):
    Simp1 = simpson(A,B,N)
    Simp2 = simpson(A,B,2*N-1)
    R = (4 * Simp2 - Simp1) / 3
    return R
              
A = 0.0
B = 1.0

maxpoints = 10e7

Nvalues = []    #empty lists
traperror = []
simpsonerror = []
rombergerror = []

exact=0.005723438559178031

N=3
while N<maxpoints:    # loop over number of points
    print(N)    #just so you can see while code is running
    Nvalues.append(N)
    traperror.append(abs(trapezoid(A,B,N)-exact)/exact)# Error in Trapezoid method
    simpsonerror.append(abs(simpson(A,B,N)-exact)/exact) # Error in Simpson method
    #rombergerror.append(abs(Romberg_extrap(A,B,N)-exact)/exact) # Error in Romberg method

    N=int(N*1.1)+1    # N grows roughly by 1.1 factor each time
    if N%2 == 0:
        N=N+1    # make sure N is odd
    
        
loglog(Nvalues,traperror,label="Trapezoid error")  # log log plot of error in trapezoid method
loglog(Nvalues,simpsonerror,label="Simpson error")  # log log plot of error in trapezoid method
#loglog(Nvalues,rombergerror,label="Romberg error")  # log log plot of error in trapezoid method
loglog(Nvalues,0.1*array(Nvalues)**(-2.0),label="0.1/N^2")   # plot 0.1/N^2 for comparison 
xlabel('Number Of Points (N)')
ylabel('|Error|')
title('Trapezoid and Simpson Integration |Error| vs N')
ylim([1e-16,1e2])   # set range of y values
legend(loc="upper right")
show()    #show the graph
