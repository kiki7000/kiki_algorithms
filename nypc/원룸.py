from sys import stdin

n, k, m = map(int, stdin.readline().split())

a = {}
for _ in range(n):
    x, y = map(int, stdin.readline().split())
    if a.get(x) is not None:
        a[x].append(y)
    else:
        a[x] = [y]
res = []
print(a)
for _ in range(m):
    b = int(stdin.readline())
    c, d = 0, 0

    i = 0
    while True:
        j = i
        e, f = 0, 0
        asdf = {}
        check = True
        while True:
            if a.get(j):
                for ii in a[j]:
                    if not asdf.get(ii):
                        asdf[ii] = True
                        e += 1
            if j == b:
                e += 1
            j += 1
            f += 1

            if e == k + 1:
                break
            if j >= len(a):
                check = False
                break
        if check:
            if d:
                d = min(d, f)
            else:
                d = f
        else:
            break
        i += 1

    res.append(d)
print("\n".join(map(str, res)))
