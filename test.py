#For loops

s=0
for n in range(1,101):
    s += 1/n
print(s)

#Emission lines
R = 1.097e-2
for m in [1,2,3]:
    print("Series for m = ",m)
    for k in range(1,6):
        n = m + k
        invlambda = R*(1/m**2 - 1/n**2)
        print("   ",1/invlambda,"nm")

#Semi-empirical mass formula
a1 = 15.8 #units of millions of eV
a2 = 18.3
a3 = 0.714
a4 = 23.2

Z = int(input("Enter the atomic number:"))
A = range(Z,3*Z+1)


for A in range(Z,3*Z+1):
    if A%2 != 0:
        a5 = 0.0

    elif Z%2 == 0:
        a5 = 12.0

    else:
        a5 = -12.0

    B = a1*A - a2*A**(2/3) - (a3*Z**2)/A**(1/3) -(a4*(A-2*Z)**2)/A + a5/A**(1/2)

    print("The binding energy per nucleon for mass number of",A," is",B/A,"MeV")




