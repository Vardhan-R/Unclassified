import math, random
x=0
y=0
for i in range (1000000):
    a=random.uniform(-1, 1)
    b=random.uniform(-1, 1)
    if (a**2 + b**2 > 1):
        y=y+1
    else:
        x=x+1
        y=y+1
print(4*x/y, math.pi)