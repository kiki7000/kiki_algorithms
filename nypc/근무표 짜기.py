n, k = map(int, input().split())
a = dict(enumerate(map(int, input().split())))
b = []

for i in map(int, input().split()):
    b.append([])
    c, j = 0, 0
    d = list(sorted(a.keys(), key=lambda x: a[x], reverse=True))[:i]

    while j < min(i, n):
        try:
            if a[d[j]] == 0:
                del a[d[j]]
            else:
                a[d[j]] -= 1
                b[-1].append(d[j] + 1)
                c += 1
            j += 1
        except:
            break

for i in b:
    print(len(i), " ".join(map(str, i)))
