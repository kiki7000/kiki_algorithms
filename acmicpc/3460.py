for _ in range(int(input())):
    a, b = list(reversed(bin(int(input()))[2:])), []
    for i in range(len(a)):
        if a[i] == "1":
            b.append(i)
            a[i] = "a"
    print(" ".join(map(str, b)))
