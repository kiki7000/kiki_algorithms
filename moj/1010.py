n, s = map(int, input().split())
for _ in range(n):
    print(" ".join(map(str, sorted(map(int, input().split()), reverse=True))))
