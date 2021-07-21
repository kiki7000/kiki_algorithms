input()
a = list(sorted(map(int, input().split())))
start, end = 0, len(a) - 1
b, c = 1000000001, 1000000001
while start < end:
    d = a[start] + a[end]
    if abs(d) < abs(b + c):
        b, c = a[start], a[end]
        if d == 0:
            break

    if d < 0:
        start += 1
    else:
        end -= 1
print(b, c)
