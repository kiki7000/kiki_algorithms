input()
a = list(sorted(map(int, input().split())))
input()
for i in list(map(int, input().split())):
    start, end = 0, len(a) - 1
    b = False
    while start <= end:
        mid = (start + end) // 2
        if a[mid] == i:
            b = True
            print(1)
            break
        elif a[mid] > i:
            end = mid - 1
        else:
            start = mid + 1
    if not b:
        print(0)
