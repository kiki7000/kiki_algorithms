from collections import defaultdict

input()
a = defaultdict(bool)

for i in map(int, input().split()):
    a[i] = True

b = int(input())
c = 0
for i in range(1, (b + 1) // 2):
    if a[i] and a[b - i]:
        c += 1

print(c)
