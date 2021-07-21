b, c = map(int, input().split())
a = 1000 / c * b

for i in range(int(input())):
    b, c = map(int, input().split())
    a = min(1000 / c * b, a)

print("%.2f" % a)
