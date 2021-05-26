a = int(input())
if a < 100:
    print(a)
else:
    r = 0
    for i in range(100, a + 1):
        b = list(map(int, str(i)))
        if b[0] - b[1] == b[1] - b[2]:
            r += 1
    print(r + 99)
