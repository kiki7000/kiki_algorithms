a = [0, 1]
for i in range(2, 41):
    a.append(a[i - 1] + a[i - 2])

for y in range(int(input())):
    b = int(input())
    if not b:
        print(1, 0)
    else:
        print(a[b - 1], a[b])
