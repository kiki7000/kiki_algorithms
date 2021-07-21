a = int(input())
b = 2
while a - 1:
    if not (a % b):
        print(b)
        a //= b
    else:
        b += 1
