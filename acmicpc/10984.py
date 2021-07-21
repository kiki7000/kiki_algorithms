for _ in range(int(input())):
    a, b = 0, 0
    for _2 in range(int(input())):
        x, y = map(float, input().split())
        a += x
        b += x * y
    a = int(a)
    print(a, round(b / a, 1))
