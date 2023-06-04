import itertools, math
n = int(input("n: "))
r = int(input("r: "))
l = []
for i in range(n):
    l.append(i + 1)

print("Permutations with repetition:")
permWithRep = itertools.product(l, repeat=r)
num = 0
for i in permWithRep:
    num = num + 1
    print(num, i)
print('\n')

print("Permutations without repetition:")
perm = itertools.permutations(l, r)
num = 0
for i in list(perm):
    num = num + 1
    print(num, i)
print('\n')

print("Combinations without repetition:")
comb = itertools.combinations(l, r)
num = 0
for i in list(comb):
    num = num + 1
    print(num, i)
print('\n')

print("Combinations with repetition:")
combWithRep = itertools.combinations_with_replacement(l, r)
num = 0
for i in list(combWithRep):
    num = num + 1
    print(num, i)
print('\n')

print("nPr with repetition =", n ** r)
print("nPr without repetition =", int((math.factorial(n))/(math.factorial(n-r))))
print("nCr without repetition =", int((math.factorial(n))/(math.factorial(r) * (math.factorial(n - r)))))
print("nCr with repetition =", int((math.factorial(n + r - 1))/(math.factorial(r) * (math.factorial(n-1)))))