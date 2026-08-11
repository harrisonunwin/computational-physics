from random import randrange

N = 1000000
double = 0

for i in range(1,N+1):
    z = randrange(1,7)
    x = randrange(1, 7)

    if z == x == 6:
        double += 1

print("A double six was rolled",double,"times")
print("The fraction of times a double six was rolled is",double/N)   #converges to roughly 1/36





