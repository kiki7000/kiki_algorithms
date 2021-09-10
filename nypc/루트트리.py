from sys import stdin

n = int(stdin.readline())
a, b, c = [False for _ in range(n + 1)], [False for _ in range(n + 1)], [[] for _ in range(n + 1)]
memo = {}


def dfs(i, prev):
    res = 1

    for j in c[i]:
        if j != prev:
            if memo.get(i * 1000000 + j):
                res += memo[i * 1000000 + j]
            else:
                res += dfs(j, i)

    memo[prev * 1000000 + i] = res
    return res


for _ in range(n - 1):
    x, y, z = map(int, stdin.readline().split())
    if not z:
        b[x - 1] = True
        b[y - 1] = True

        c[x - 1].append(y - 1)
        c[y - 1].append(x - 1)
    else:
        c[x - 1].append(y - 1)
        a[y - 1] = True

d = []
for i in range(n):
    if not a[i] and not b[i]:
        d.append(i)

if len(d) > 1:
    print(0)
else:
    if not d:
        for i in range(n):
            if not a[i]:
                d.append(i)

    d = list(set(d))
    res = 0

    for i in d:
        if dfs(i, -1) == n:
            res += 1

    print(res)
