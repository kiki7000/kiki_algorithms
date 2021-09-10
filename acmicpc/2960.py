n, k = map(int, input().split())
a = [False, False] + [i for i in range(2, n + 1)]
b = []
for i in range(2, n + 1):
    for j in range(i, n + 1, i):
        if a[j]:
            b.append(j)
            a[j] = False
print(b[k - 1])
