for _ in range(int(input())):
    a, b = map(int, input().split())
    num = 1

    while not (num ** 2 <= b - a < (num + 1) ** 2):
        num += 1

    if num ** 2 == b - a:
        print(num * 2 - 1)
    elif num ** 2 < b - a <= num ** 2 + num:
        print(num * 2)
    else:
        print(num * 2 + 1)
