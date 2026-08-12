
from matplotlib import pyplot as plt
from random import random
import matplotlib.animation as animation

L = 101
steps = 1000000
i = j = L//2        #start points in centre of grid
i_steps, j_steps = [i], [j]


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

    i_steps.append(i)
    j_steps.append(j)

print("The particle is situated at point",i,j)

#set up grid
fig, ax = plt.subplots()
ax.set_xlim(0, L - 1)
ax.set_ylim(0, L - 1)
ax.set_aspect('equal')
ax.grid(True, linestyle='--', alpha=0.4)

trail, = ax.plot([], [], linewidth=0.5)       # the path so far
point, = ax.plot([], [], 'ro')

def update(frame):
    trail.set_data(i_steps[:frame+1], j_steps[:frame+1])
    point.set_data([i_steps[frame]], [j_steps[frame]])
    return trail, point

ani = animation.FuncAnimation(
    fig, update, frames=len(i_steps), interval=20, blit=True
)

plt.show()
