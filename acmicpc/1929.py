a, b = map(int, input().split())
c = [False, False] + [i for i in range(2, b + 1)]
for i in range(2, b + 1):
    if not c[i]:
        continue
    for j in range(i * 2, b + 1, i):
        c[j] = False

for i in range(a, b + 1):
    if c[i]:
        print(i)
