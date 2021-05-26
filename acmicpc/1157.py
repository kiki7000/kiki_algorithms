n = input().lower().count
a = {chr(i): n(chr(i)) for i in range(97, 123)}
b = max(a.values())
c, d = 0, "?"

for i in a:
    if a[i] == b:
        c += 1
        d = i

if c == 1:
    print(d.upper())
else:
    print("?")
