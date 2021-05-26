a = -1
b = -1

for i in range(9):
    k = int(input())
    if k > a:
        a = k
        b = i + 1

print(a)
print(b)
