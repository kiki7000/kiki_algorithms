a = {chr(i): 0 for i in range(65, 92)}
for _ in range(int(input())):
    b = input()

    for i in range(0, len(b)):
        a[b[i]] += 10 ** (len(b) - i - 1)

a_ = a.copy()
for i in a_:
    if not a_[i]:
        del a[i]

b, c = 9, 0
for i in sorted(a, key=lambda x: a[x], reverse=True):
    c += a[i] * b
    b -= 1

print(c)
