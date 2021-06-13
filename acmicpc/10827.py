a, b = input().split()
b, c = int(b), len(a) - a.index(".") - 1
a = int(a.replace(".", ""))

d = str(a ** b)
e = len(d) - len(str((10 ** c) ** int(b))) + 1
if e >= 0:
    print(d[:e] + "." + d[e:])
else:
    print("0." + "0" * -e + d)
