_, a = map(int, input().split())
b, c = list(sorted(map(int, input().split()))), 100001
for i in range(0, len(b)):
    for j in range(i + 1, len(b) + 1):
        d = sum(b[i:j])
        if d >= a:
            c = min(c, j - i)
            break
print(c)
