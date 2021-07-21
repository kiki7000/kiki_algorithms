a, b = int(input()), 0
for i in range(a):
    for j in range(i, a // (i + 1)):
        b += 1
print(b)
