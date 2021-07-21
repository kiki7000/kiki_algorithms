a, b = int(input()), int(input())
start, end = 1, a ** 2
c = -1

while start <= end:
    mid = (start + end) // 2
    if sum([min(a, mid // i) for i in range(1, a + 1)]) < b:
        start = mid + 1
    else:
        end = mid - 1
        if c != -1:
            c = min(c, mid)
        else:
            c = mid
print(c)
