from collections import Counter

a, b = [], []
for _ in range(3):
    c, d = map(int, input().split())
    a.append(c)
    b.append(d)
print(Counter(a).most_common()[1][0], Counter(b).most_common()[1][0])
