_, a = map(int, input().split())
b = 0

for i in map(int, input().split()):
    if a < i:
        break

    a -= i
    b += 1

print(b)
