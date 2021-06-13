a, b = input(), input()
c = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]

for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            c[i + 1][j + 1] = c[i][j] + 1
        else:
            c[i + 1][j + 1] = max(c[i][j + 1], c[i + 1][j])

print(c[len(a)][len(b)])
