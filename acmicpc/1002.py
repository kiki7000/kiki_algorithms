for _ in range(int(input())):
    a, b, c, d, e, f = map(int, input().split())
    if c > f:
        c, f = f, c

    g = ((a - d) ** 2 + (b - e) ** 2) ** 0.5
    r = None
    if g <= f:
        if a == d and b == e and c == f:
            r = -1
        elif c + g == f:
            r = 1
        elif c + g > f:
            r = 2
        else:
            r = 0
    else:
        if c + f < g:
            r = 0
        elif c + f > g:
            r = 2
        else:
            r = 1

    print(r)
