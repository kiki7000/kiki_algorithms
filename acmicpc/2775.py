for _ in range(int(input())):
    a = int(input())
    b = int(input())
    c = list(range(1, b + 1))

    for i in range(a):
        for j in range(1, b):
            c[j] += c[j - 1]

    print(c[b - 1])
