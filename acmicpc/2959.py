a = list(map(int, input().split()))
a.remove(max(a))

print(max(a) * min(a))
