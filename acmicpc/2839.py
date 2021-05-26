a = int(input())
b = False

for i in range(a // 5, -1, -1):
    if not (a - i * 5) % 3:
        print(i + (a - i * 5) // 3)
        b = True
        break

if not b:
    print(-1)
