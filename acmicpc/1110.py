a = int(input())
b, c = 0, a

while a != c and not b:
    b += 1
    c = (c % 10) * 10 + (c // 10 + c % 10) % 10

print(b)
