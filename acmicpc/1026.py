input()
a = sorted(map(int, input().split()))
b = sorted(map(int, input().split()), reverse=True)
c = 0

for i in range(len(a)):
    c += a[i] * b[i]

print(c)
