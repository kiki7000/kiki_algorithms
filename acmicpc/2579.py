a = [0] + [int(input()) for _ in range(int(input()))] + [0]
b = [0, a[1], a[1] + a[2]]
for i in range(3, len(a) - 1):
    b.append(max(b[i - 3] + a[i - 1], b[i - 2]) + a[i])
print(b[-1])
