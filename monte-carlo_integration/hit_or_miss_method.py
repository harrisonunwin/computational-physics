from random import random
from math import sin, sqrt

def f(x):
    s = sin(1/(x*(2-x)))**2
    return s

N = 10000
area = 2

def monte_carlo():
    count = 0
    for i in range(N):
        x = area*random()
        y = random()
        if y < f(x):
            count += 1

    I = area * count / N
    return I

def error(I):
    std = sqrt(I * (area - I) / N)
    return std

def main():
    I = monte_carlo()
    std = error(I)
    print("Value of integral is",I)
    print("Error is",std)
main()




