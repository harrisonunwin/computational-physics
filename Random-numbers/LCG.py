import matplotlib.pyplot as plt

#Linear congruential random number generator
#not actually random

N = 100
a = 1664525       #values for a,c,m are important
c = 1013904223
m = 4294967296
x = 1
results = []

for i in range(N):
    x = (a*x + c) % m
    results.append(x)

plt.plot(results,"o")
plt.show()