x,y=1,3
print(f"The value of x is {x} and the value of y is {y}")

#Seperator, inputs where the commas are
w = 3.14159
z = 1+2j
print("We can separate variables using sep:",w,z,sep="___")

#modulo operation
u = 26%3
print("The remainder of 26/3 is",u)

#Can update variables
x = x + 1
print("The updated value of x is",x)

#Python modifiers
"x += 1"
"x -= 4"
"x *= 2.5"
"x /= 4"
"x //= 3.2"

#We can swap variables
x,y = y,x
print("Now we have swapped the value of x and y, so x =",x,"and y =",y)

#Ball drop
from math import sqrt, pi
height = float(input("Please enter your height in meters:"))
g = 9.81
time = sqrt(2*height/g)
print(f"The time it takes for the ball to reach the ground is: {time}")


#Altitude for orbit with time period T

G = 6.67e-11
M = 5.97e24
R = 6.371e6
T = float(input("Please enter the time period your orbit in seconds:"))
h = (G*M*T**2/(4*pi**2))**(1/3) - R
print(f"The height of your obit is: {h}")



