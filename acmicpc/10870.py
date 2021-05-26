a = [0, 1, 1]
b = int(input())
if b < 3:
    print(a[b])
else:
    for i in range(len(a), b + 1):
        a.append(a[i - 1] + a[i - 2])

    print(a[b])
