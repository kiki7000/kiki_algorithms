for _ in range(int(input())):
    a, b = int(input().split()[1]), list(map(int, input().split()))
    print(sum([i // a for i in b]))
