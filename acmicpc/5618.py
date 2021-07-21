def gcd(a, b):
    a, b = min(a, b), max(a, b)
    while True:
        if not (b % a):
            return a
        a, b = b % a, a


n = int(input())
if n == 2:
    a = gcd(*map(int, input().split()))
else:
    b = list(map(int, input().split()))
    a = gcd(b[0], gcd(b[1], b[2]))

print(1)
for i in range(2, a // 2 + 1):
    if not (a % i):
        print(i)
if a != 1:
    print(a)
