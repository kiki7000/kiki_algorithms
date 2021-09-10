input()
a = input()[1:-1]
b, c = a[0], ""
for i in a:
    if i == b:
        c += "0"
    else:
        c += "1"
print(c)
