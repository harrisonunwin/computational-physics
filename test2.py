#How to load text files

from numpy import loadtxt

a = loadtxt("values.txt", float, delimiter=" ")
print(a)