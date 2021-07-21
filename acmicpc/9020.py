a = [False, False] + [i for i in range(2, 10001)]
for i in range(2, 10001):
    if not a[i]:
        continue
    for j in range(i * 2, 10001, i):
        a[j] = False

for _ in range(int(input())):
    b = int(input()) // 2
    c = 0
    while True:
        if a[b + c] and a[b - c]:
            print(b - c, b + c)
            break
        c += 1
