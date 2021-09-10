input()
a, b = 0, -10000000000000000000000000000000

for i in map(int, input().split()):
    a = max(0, a) + i
    b = max(a, b)
print(b)
