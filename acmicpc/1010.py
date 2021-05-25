a = [[0] * 30 for i in range(30)]
a[1][1:] = [i for i in range(1, 30)]

for i in range(2, 30):
    for j in range(i, 30):
        for k in range(i - 1, j):
            a[i][j] += a[i - 1][k]

for _ in range(int(input())):
    b, c = map(int, input().split())
    print(a[b][c])
