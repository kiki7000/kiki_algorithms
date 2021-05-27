def compare(lis, a):
    for i in lis:
        if i[a] != lis[0][a]:
            return False
    return True


a = int(input())
b, c = [], ""

for i in range(a):
    b.append(input())

for i in range(len(b[0])):
    if compare(b, i):
        c += b[0][i]
    else:
        c += "?"

print(c)
