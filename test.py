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


