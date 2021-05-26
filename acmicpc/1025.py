a, b = map(int, input().split())
c, d = -1, []

for _ in range(a):
    d.append(list(map(int, input())))

for w in range(a):
    for x in range(b):
        for y in range(1 - a, a):
            for z in range(1 - b, b):
                num = d[w][x]

                if int(num ** 0.5) ** 2 == num:
                    c = max(c, num)
                if not y and not z:
                    continue

                i, j = w, x
                while 0 <= i + y < a and 0 <= j + z < b:
                    num = num * 10 + d[i + y][j + z]
                    if int(num ** 0.5) ** 2 == num:
                        c = max(c, num)

                    i += y
                    j += z

print(c)
