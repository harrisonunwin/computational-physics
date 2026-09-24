from math import sqrt
from random import random

def f(x):
    return sum(i**2 for i in x)

R = 1
N = int(1e6)
D = 10
area = (2*R)**D

def montecarlo():
    count = 0
    for i in range(N):
        point = (2*R*random() - R for _ in range(D))
        if f(point) <= R**2:
            count += 1

    return area * count / N

print(montecarlo())




