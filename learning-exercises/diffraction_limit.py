import numpy as np
import matplotlib.pyplot as plt

def J(m,x):
    N = 1000
    a = 0
    b = np.pi
    h = (b - a) / N

    def integrand(theta):
        return np.cos(m*theta -x*np.sin(theta))

    s = integrand(a) + integrand(b)

    for k in range(1,N,2):
        s += 4*integrand(a + k*h)

    for k in range(2,N,2):
        s += 2*integrand(a + k*h)

    return (1/3)*h*s*(1/np.pi)

x_values = np.linspace(0,20,1000)

for m in range(0,3):
    y_values = []
    for x in x_values:
        y_values.append(J(m,x))
    plt.plot(x_values, y_values, label=f"m = {m}")

plt.xlabel('x')
plt.ylabel('J_m(x)')
plt.legend()
plt.show()


