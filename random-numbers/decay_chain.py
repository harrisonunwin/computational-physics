from random import random
from numpy import arange
import matplotlib.pyplot as plt

N_Bi = 10000
N_Tl = 0
N_Pb = 0
tau_Bi = 132  #half-life of Bi-213 in seconds
dt = 1.0
p = 1 - 2**(-dt/tau_Bi)     #Probability of decay in one time interval
tmax = 1000         #maximum time


points_time = arange(0,tmax,dt)
points_Bi = []
points_Tl = []
points_Pb = []

for t in points_time:
    points_Tl.append(N_Tl)
    points_Pb.append(N_Pb)
    points_Bi.append(N_Bi)

    decay_Tl = 0
    decay_Pb = 0
    for i in range(N_Bi):
        if random() < p:
            if random() < 0.0209:
                decay_Tl += 1

            else:
                decay_Pb += 1

    N_Bi -= decay_Tl + decay_Pb
    N_Tl += decay_Tl
    N_Pb += decay_Pb

#Plot the graph
plt.plot(points_time, points_Bi, label='Bi-213')
plt.plot(points_time, points_Tl, label='Tl-209')
plt.plot(points_time, points_Pb, label='Pb-209')
plt.xlabel('Time (s)')
plt.ylabel('Number of atoms')
plt.title('Radioactive Decay Chain: Bi-213 → Tl-209/Pb-209')
plt.legend()
plt.show()
