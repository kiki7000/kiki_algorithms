a = {}
input()
b = input().split()
c, d = {str(i): [] for i in range(len(b))}, {str(i): 0 for i in range(len(b))}

for i in range(len(b)):
    f = b[i]
    a[str(i)] = f

    if f != "-1":
        c[f].append(str(i))
        d[f] += 1


def keep_delete(n):
    for i in c[n]:
        d[n] -= 1
        keep_delete(i)
    a[n]
    del c[n]
    if a[n] != "-1":
        d[a[n]] -= 1
    del a[n]


keep_delete(input())
c = 0
for i in a:
    if not d[i]:
        c += 1
print(c)
