a, b = map(int, input().split())

if b < 45:
    b += 15
    a -= 1
else:
    b -= 45

if a < 0:
    a = 23

print(a, b)
