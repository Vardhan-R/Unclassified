import math
x=-1
y=1
for i in range(math.floor(float(input('num? ')))):
    z=x+y
    if y!=0:
        r=z/y
    else:
        r='N/A'
    print(i+1, z, r)
    x=y
    y=z