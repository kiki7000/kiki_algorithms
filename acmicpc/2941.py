a = input()
b = 0

for i in ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]:
    b += a.count(i)
    a = a.replace(i, " ")

print(b + len(a.replace(" ", "")))
