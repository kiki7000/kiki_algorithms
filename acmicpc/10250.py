for _ in range(int(input())):
    a, b, c = map(int, input().split())
    b = c % a
    c = c // a + 1

    if not b:
        b = a
        c -= 1

    print(b * 100 + c)
