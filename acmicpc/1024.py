a, b = map(int, input().split())
c, d, e = 0, -1, 0

for i in range(b, 101):
    c = (i * (i - 1)) / 2
    if (a - c) % i == 0 and (a - c) // i >= 0:
        d = (a - c) // i
        e = i
        break

if d == -1:
    print(-1)
else:
    for i in range(e):
        print(int(d + i), end=" ")
