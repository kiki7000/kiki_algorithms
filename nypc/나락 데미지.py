n = int(input())
a = []

for _ in range(n):
    a.append(list(map(int, input().split())))

b = list(sorted(a, key=lambda x: x[0]))
a = [i[0] for i in a]
dp = [b[0][0] ** 2]
res = {b[0][0]: dp[0]}

for i in range(1, n):
    c = []
    mn = 1000000000000000000000000000000000000000000000
    for j in range(i):
        if not (b[j][2] < b[i][1] or b[j][1] > b[i][2]):
            mn = min(mn, (b[i][0] - b[j][0]) ** 2 + b[j][3] + dp[j])
    dp.append(min(mn, b[i][0] ** 2))
    res[b[i][0]] = dp[i]

for i in a:
    print(res[i])
