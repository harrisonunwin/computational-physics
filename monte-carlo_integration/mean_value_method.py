from random import random
from math import sin, sqrt

#Using mean-value method to evaluate integral of pathological function

def f(x):
    '''Pathological function'''
    s = sin(1/(x*(2-x)))**2
    return s

N = 10000
a = 0
b = 2

def summation():
    '''Calculates the sum of f(x), and of f(x)**2'''
    sum = 0
    sum_squared = 0
    for i in range(N):
        x = 2 * random()
        fx = f(x)
        sum += fx
        sum_squared += fx**2
    return sum, sum_squared

sum, sum_squared = summation()

def integral():
    return ((b-a)*sum)/N

def variance():
    '''Calculates the variance of f(x)'''
    mean = sum/N
    squared_mean = sum_squared/N
    var = squared_mean - mean**2
    return var

def error():
    '''Calculates the error of integral'''
    return (b-a)*sqrt(variance()/N)

integral = integral()
error = error()
variance = variance()

print("Integral: ", integral)
print("Error: ", error)
print("Variance: ", variance)




