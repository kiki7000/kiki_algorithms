from sys import stdin
from heapq import heappop, heappush

a = []
for _ in range(int(stdin.readline())):
    b = int(stdin.readline())
    if not b:
        if not a:
            print(0)
        else:
            print(heappop(a) * -1)
        continue
    heappush(a, b * -1)
