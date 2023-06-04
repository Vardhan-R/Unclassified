d1, d2 = {"a": "p", "b": "q", "c": "r"}, {}
for i in d1.keys(): d2[d1[i]] = i
print(d1)
print(d2)