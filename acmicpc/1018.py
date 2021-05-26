a, b = map(int, input().split())


def getPan(pan):
    br, wr = "BW" * 4, "WB" * 4
    res1, res2 = 0, 0

    a = True
    for i in pan:
        b = br if a else wr
        a = not a
        for j in range(8):
            if b[j] != i[j]:
                res1 += 1

    a = False
    for i in pan:
        b = br if a else wr
        a = not a
        for j in range(8):
            if b[j] != j[j]:
                res2 += 1

    return min(res1, res2)


n = []
res = []
for i in range(a):
    n.append(input())

for x in range(0, b - 7):
    for y in range(0, a - 7):
        res.append(getPan([i[x : x + 8] for i in n[y : y + 8]]))

print(min(res))
