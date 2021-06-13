from collections import deque

a = int(input())
b = deque(map(int, input().split()))
c, d, e = [], [], [0 for _ in range(500011)]

for i in range(a):
    f = b.pop()

    while c and (c[-1] <= f):
        c.pop()
        e[d.pop()] = a - i

    c.append(f)
    d.append(a - i)

print(" ".join(map(str, e[1 : a + 1])))
