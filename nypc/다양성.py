from sys import stdin

n, k = map(int, stdin.readline().split())
a = list(map(int, stdin.readline().split()))
if k <= 10:
    b = -1
    c = {}
    for i in range(0, n - k + 1):
        r = 0
        for j in range(i, i + k):
            for ii in range(j, i + k):
                r += abs(a[j] - a[ii])
        if b == -1:
            b = r
        else:
            b = max(b, r)
    print(b)
else:
    b = [[] for _ in range(n)]

    for i in range(0, n):
        for j in range(0, n):
            if j > 0:
                b[i].append(b[i][j - 1] + abs(a[i] - a[j]))
            else:
                b[i].append(abs(a[j] - a[i]))

    m = -1
    for i in range(0, n - k + 1):
        r = 0
        for j in range(k):
            r += b[i + j][i + k - 1] - b[i + j][i + j]
        m = max(m, r)
    print(m)
