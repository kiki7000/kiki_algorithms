n, m = map(int, input().split())
a = []
b = []
asdf = []

for i in range(n):
    b.append(list(map(int, input().split())))

while True:
    c = True
    for i in b:
        for j in i:
            if j != 0:
                c = False
                break
        if not c:
            break
    if c:
        break

    c, d, e = None, 0, -1

    # HORIZONTAL SEARCH
    for d in range(n):
        f, g = -1, True
        for j in b[d]:
            if not j:
                continue
            if f == -1:
                f = j
            elif j != f:
                g = False
                break
        if g and f != -1:
            c = "H"
            e = f
            for j in range(len(b[d])):
                b[d][j] = 0
            break

    if c is None and e == -1:
        # VERTICAL SEARCH
        for d in range(m):
            f, g = -1, True
            for j in b:
                if not j[d]:
                    continue
                if f == -1:
                    f = j[d]
                elif j[d] != f:
                    g = False
                    break

            if g and f != -1:
                c = "V"
                e = f
                for j in range(len(b)):
                    b[j][d] = 0
                break

    a.append([c, d + 1, e])

print(len(a))
for i in reversed(a):
    print(i[0], i[1], i[2])
