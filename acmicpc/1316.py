a = 0

for i in range(int(input())):
    b = input()
    a += list(b) == sorted(b, key=b.find)

print(a)
