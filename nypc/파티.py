from sys import stdin

n = int(input())
m = list(sorted(map(int, stdin.readline().split()), reverse=True))
a = sum(m)
if not a % n:
    b, c = a // n, a // n
else:
    b, c = a // n + 1, a // n
d, e = 0, 0

for i in m:
    if b >= i:
        break
    d += i - b

for i in reversed(m):
    if i >= c:
        break
    e += c - i

print(max(d, e))
