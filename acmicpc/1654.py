a, b = map(int, input().split())
c = [int(input()) for _ in range(a)]
d, e = sum(c) // b, 1

while e <= d:
    f = (d + e) // 2
    g = sum(map(lambda x: x // f, c))

    if g >= b:
        e = f + 1
    else:
        d = f - 1
print(d)
