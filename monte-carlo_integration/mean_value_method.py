from random import random
from math import sin, sqrt


def f(x):
    s = sin(1/(x*(2-x)))**2
    return s

N = 10000
a = 0
b = 2

def sum():
    sum = 0
    for i in range(N):
        x = 2 * random()
        sum += f(x)
    return sum

def integral():
    return ((b-a)*sum())/N

integral = integral()

print(integral)

