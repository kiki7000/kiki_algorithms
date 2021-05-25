for i in range(int(input())):
    a, b, c, d = map(int, input().split())
    n = 0

    for i in range(int(input())):
        f, g, h = map(int, input().split())
        if (
            (
                (((a - f) ** 2) + ((b - g) ** 2)) ** 0.5 < h
                and (((c - f) ** 2) + ((d - g) ** 2)) ** 0.5 > h
            )
            or (((a - f) ** 2) + ((b - g) ** 2)) ** 0.5 > h
            and (((c - f) ** 2) + ((d - g) ** 2)) ** 0.5 < h
        ):
            n += 1

    print(n)
