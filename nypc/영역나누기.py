from sys import stdin
from heapq import heappop, heappush

n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))
b = [False for _ in range(n + 1)]
c = [0 for _ in range(n + 1)]

d = n * (n - 1) // 2
e = set([])
f = 0

for i in range(2 * n):
    j = a[i]
    if not b[j]:
        b[j] = True
        c[j] = i
        e.add(i)
    else:
        start, end = 0, len(e)
        while start <= end:
            mid = (start + end) // 2
            if e[mid] > c[j] and e[mid - 1] <= c[j]:
                break
            elif e[mid] > c[j]:
                end = mid - 1
            else:
                start = mid + 1
        f += len(e) - mid + 1
        e.remove(c[j])

print(f + n + 1)
