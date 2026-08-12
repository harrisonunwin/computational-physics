#radioactive decay using transformation method

from random import random
from math import log
from matplotlib import pyplot as plt
from numpy import sort

N = 10000       #number of atoms initially
tau = 183.16    #half-life

def f(z):          #Produces time of atom decay
    mu = log(2)/tau
    x = -(1/mu)*log(1-z)
    return x

decay_times = []

for i in range(N):
    z = random()
    decay_times.append(f(z))

decay_sorted = sort(decay_times)                  #sorts decay times
plt.plot(decay_sorted, range(N,0,-1))       #counts down to show atoms remaining
plt.xlabel('Time')
plt.ylabel('No. of atoms remaining')
plt.show()

