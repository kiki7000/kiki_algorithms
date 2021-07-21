for _ in range(int(input())):
    a = int(input())
    b, c, d = 0, 0, 0

    b = a // 25
    a %= 25

    c = a // 10
    a %= 10

    d = a // 5
    a %= 5

    print(b, c, d, a)
