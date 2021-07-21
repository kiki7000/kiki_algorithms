input()
a, b = input(), 0
for i in range(len(a)):
    b += (ord(a[i]) - 96) * (31 ** i)
print(b % 1234567891)
