l1 = []
l2 = []
n = []
u = []
while True:
    x = input('"done" to cancel (l1) ')
    if x == "done":
        break
    elif x not in l1:
        l1.append(x)
while True:
    x = input('"done" to cancel (l2) ')
    if x == "done":
        break
    elif x not in l2:
        l2.append(x)
l1.sort()
l2.sort()
for i in l1:
    u.append(i)
    if i in l2:
        n.append(i)
for i in l2:
    if i not in u:
        u.append(i)
n.sort()
u.sort()
print(l1)
print(l2)
print(n)
print(u)