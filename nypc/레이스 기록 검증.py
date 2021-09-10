n, m = map(int, input().split())
a, c = {}, True

for _ in range(m):
    b = list(map(int, input().split()))
    if a.get(b[1]):
        if b[0] - a[b[1]][0] < 60:
            c = False
        elif a[b[1]][1] == b[2]:
            c = False
        else:
            a[b[1]] = None
    else:
        if b[2] == 1:
            c = False
        else:
            a[b[1]] = [b[0], b[2]]

if len(list(filter(lambda x: a[x] is not None, a))):
    c = False
if c:
    print("YES")
else:
    print("NO")
