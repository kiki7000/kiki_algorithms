for _ in range(int(input())):
    a, b = map(int, input().split())
    res = 1

    for j in range(b):
        res = res * a % 10

    if not res:
        print(10)
    else:
        print(res)
