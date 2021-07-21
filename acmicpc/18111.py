from sys import stdin

a, _, b = map(int, stdin.readline().split())
c = {}
for _ in range(a):
    for i in map(int, stdin.readline().split()):
        if c.get(i):
            c[i] += 1
        else:
            c[i] = 1
d, e = 1000000000000000000000000000000, -1
for i in range(257):
    f, g = 0, 0
    for j, k in c.items():
        if j > i:
            f += (j - i) * k
        elif j < i:
            g += (i - j) * k
    if f * 2 + g <= d and b + f - g >= 0:
        d = f * 2 + g
        e = i
print(d, e)
