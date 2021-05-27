a, b, c = map(int, input().split())
d = 0
while b != c:
    b -= b // 2
    c -= c // 2
    d += 1

print(d)
