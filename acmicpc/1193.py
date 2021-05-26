a = int(input())
b, c = 1, 1
while b + c <= a:
    c += b
    b += 1

d = a - c
e, f = a - c + 1, -a + b + c
if not b % 2:
    print(f"{e}/{f}")
else:
    print(f"{f}/{e}")
