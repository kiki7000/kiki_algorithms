from collections import deque

for _ in range(int(input())):
    __, a = map(int, input().split())
    b = deque(map(list, enumerate(map(int, input().split()))))
    c, d = deque(reversed(sorted(b, key=lambda x: x[1]))), 1

    while True:
        if b[0][1] != c[0][1]:
            b.append(b.popleft())
            continue

        c.popleft()
        if b[0][0] != a:
            d += 1
            b.popleft()
        else:
            print(d)
            break
