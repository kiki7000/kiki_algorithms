def b(x, y, z):
    if not x:
        return
    b(x - 1, y, 6 - (y + z))
    print(y, z)
    b(x - 1, 6 - (y + z), z)


a = int(input())
print((1 << a) - 1)
b(a, 1, 3)
