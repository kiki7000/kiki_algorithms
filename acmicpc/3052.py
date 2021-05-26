a = {}
for _ in range(10):
    b = int(input()) % 42
    if b in a:
        a[b] += 1
    else:
        a[b] = 1
print(len(a))
