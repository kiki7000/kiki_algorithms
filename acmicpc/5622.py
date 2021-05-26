a = {chr(i): ((i - 1) // 3) - 30 for i in range(97, 121)}
a["y"] = 9
a["z"] = 9

b = 0
for i in input():
    b += a[i.lower()] + 1

print(b)
