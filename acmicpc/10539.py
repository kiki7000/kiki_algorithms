input()
a = list(map(int, input().split()))
b = 0
for i in range(len(a)):
    print((i + 1) * a[i] - b, end=" ")
    b += (i + 1) * a[i] - b
