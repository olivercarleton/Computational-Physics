from pylab import *

def func(x):
    return exp(-x)

def trapezoid(A, B, N):
    h = (B - A) / (N - 1)
    sum = (func(A) + func(B)) / 2
    for i in range(1, N - 1):
        sum += func(A + i * h)
        sum = float32(sum)
    return h * sum

def simpson(A, B, N):
    if (N - 1) % 2 == 1:
        print("Simpson's rule requires even number of intervals")
        return 0
    h = (B - A) / (N - 1)
    sum = (func(A) + func(B)) / 3
    for i in range(1, N - 1, 2):
        sum += 4 / 3 * func(A + i * h)
        sum = float32(sum)
    for i in range(2, N - 1, 2):
        sum += 2 / 3 * func(A + i * h)
        sum = float32(sum)
    return h * sum

A = 0.0
B = 1.0

maxpoints = 10000000

Nvalues = []
traperror = []
simpsonerror = []

exact = 1 - exp(-1)

N = 3
while N < maxpoints:
    print(N)
    Nvalues.append(N)
    traperror.append(abs(trapezoid(A, B, N) - exact) / exact)
    simpsonerror.append(abs(simpson(A, B, N) - exact) / exact)
    N = int(N * 1.1) + 1
    if N % 2 == 0:
        N = N + 1

loglog(Nvalues, traperror, label="Trapezoid error")
loglog(Nvalues, simpsonerror, label="Simpson error")
loglog(Nvalues, 0.1 * array(Nvalues) ** (-2.0), label="0.1/N^2")
xlabel('Number of Points (N)')
ylabel('|Error|')
title('Trapezoid and Simpson Integration |Error| vs N')
ylim([1e-8,1])
legend(loc="lower left")
show()



