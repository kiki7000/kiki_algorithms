for _ in range(int(input())):
    a = list(filter(lambda x: not x % 2, map(int, input().split())))
    print(sum(a), min(a))
