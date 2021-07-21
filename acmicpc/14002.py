from bisect import bisect_left

input()
a = list(map(int, input().split()))
b, c, d = [], [], []


for i in a:
    if len(b) == 0 or b[-1] < i:
        b.append(i)
        c.append(len(b) - 1)
    else:
        b[bisect_left(b, i)] = i
        c.append(bisect_left(b, i))
    d.append(i)

e = len(b) - 1
f = []
for i in range(len(c) - 1, -1, -1):
    if c[i] == e:
        e -= 1
        f.append(d[i])
print(len(f))
print(" ".join(reversed(list(map(str, f)))))
