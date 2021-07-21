a, b = list(map(int, input().split())), list(map(int, input().split()))
c, d, e = 0, 0, -1
for i in range(len(a)):
    if a[i] > b[i]:
        e = i
        c += 3
    elif a[i] < b[i]:
        e = i
        d += 3
    else:
        c += 1
        d += 1

print(c, d)
if e == -1:
    print("D")
elif (c == d and a[e] > b[e]) or c > d:
    print("A")
else:
    print("B")
