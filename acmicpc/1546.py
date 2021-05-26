input()

a = list(map(int, input().split()))
m = max(a)

print(round(sum(map(lambda i: (i / m) * 100, a)) / len(a), 2))
