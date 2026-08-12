#Create LxL lattice
from matplotlib import pyplot as plt
from random import random

L = 101
steps = 1000000
j_points = range(L)
i_points = range(L)

i,j = 50,50    #start points in centre of grid


for s in range(steps):

    if random() < 0.5:
        if random() < 0.5:
            if i < L-1:
                i += 1
        else:
            if i > 0:
                i -= 1

    else:
        if random() < 0.5:
            if j < L-1:
                j += 1
        else:
            if j > 0:
                j -= 1



print(i,j)
