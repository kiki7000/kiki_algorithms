def ob(a):
    res = 0
    while a:
        res += a % 2
        a //= 2
    return res


a, b = map(int, input().split())
if ob(a) <= b:
    print(0)
else:
    c, d = 2, 0
    while True:
        if a % c:
            a += c // 2
            d += c // 2
            if ob(a) <= b:
                break
        c *= 2

    print(d)
