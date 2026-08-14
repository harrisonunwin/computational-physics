from random import random
from math import sin

def f(x):
    s = sin(1/(x*(2-x)))**2
    return s

def main():
    N = 10000
    count = 0
    for i in range(N):
        x = 2*random()
        y = random()
        if y < f(x):
            count += 1

    I = 2*count/N
    print("The value of the integrl is",I)
main()




