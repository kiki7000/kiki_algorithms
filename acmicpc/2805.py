_, a = map(int, input().split())
b = list(sorted(map(int, input().split())))
c, d = 0, 1000000000
e = (c + d) // 2

while c <= d:
    f = 0
    for i in b:
        f += max(0, i - e)
    if f >= a:
        c = e + 1
    else:
        d = e - 1
    e = (c + d) // 2
print(e)
