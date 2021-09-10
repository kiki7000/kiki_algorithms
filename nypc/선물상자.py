n, m = map(int, input().split())
d = list(map(int, input().split()))
a = []
for i in range(n):
    a.append([i, d[i]])
prev = -1
l = n
while True:
    prev = (prev + m) % len(a)
    a[prev][1] -= 1
    if a[prev][1] == 0:
        del a[prev]
    if len(a) == 1:
        break

print(a[0][0] + 1)
