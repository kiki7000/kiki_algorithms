a, b = map(int, input().split())
c = 0
d = list(map(int, input().split()))

for i in range(a - 2):
    for j in range(i + 1, a - 1):
        for k in range(j + 1, a):
            if c < d[i] + d[j] + d[k] <= b:
                c = d[i] + d[j] + d[k]

print(c)
