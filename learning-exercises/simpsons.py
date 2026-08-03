from scipy.integrate import simpson
from numpy import linspace

def f(x):
    return x**4 - 2*x +1

N=10
a=0
b=2
h=(b-a)/N

s = f(a)+f(b)
for k in range(1,N,2):
    s += 4*f(a+k*h)
for k in range(2,N,2):   #Previous mistake, make sure second loop is not nested inside first.
        s += 2*f(a+k*h)

print((1/3)*h*s)

#scipy check
x = linspace(a,b,N+1)
y = f(x)
scipy_result = simpson(y,x)
print(scipy_result)

