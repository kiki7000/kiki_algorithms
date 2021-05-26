a = int(input())
b, c, d = 1, 6, 1

if a == 1:
    print(1)
else:
    while True:
        b += c
        c += 6
        d += 1

        if a <= b:
            print(d)
            break
