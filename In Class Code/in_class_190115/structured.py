

b = [1, 3, 5, 7, 11, 13]

for x in b:
    print(x, x*x)


d = {"a": "able", "b": "baker", "d": "dog", "c": "charlie"}

for x in d:
    print(x, d[x])

print(15*"+")

for x in sorted(d):
    print(x, d[x])

print(15*"+")

for (x,y) in d.items():
    print(x, y)


print(range(10))
for x in range(10):
    print(x)

