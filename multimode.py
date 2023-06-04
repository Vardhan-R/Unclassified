import random

k = []
x = 0
c = 0
d = {}
l = []

for i in range (6):
    k.append(random.randint(0, 3))

for i in k:
    c = 0
    for j in k:
        if i == j:
            c = c + 1
    d[i] = c

for i in d:
    if d[i] > x:
        l.clear()
        x = d[i]
    if d[i] == x:
        l.append(i)

l.sort()

print(k)
print(d)
print(l)