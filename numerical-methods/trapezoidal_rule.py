from numpy import loadtxt
from numpy import trapezoid

data = loadtxt("velocities.txt", delimiter="\t")

xdata = data[:,0] #time data
ydata = data[:,1] #velocities data

h = (xdata[-1]-xdata[0])/(len(xdata)-1) #one second intervals

s = 0.5*ydata[0] + 0.5*ydata[-1] #Trapezoidal rule
for k in range(1,len(xdata)-1):
    s += ydata[k]

print("The particle has travelled a distance of",h*s,"meters.")

print(trapezoid(ydata, xdata)) #To check against our value





