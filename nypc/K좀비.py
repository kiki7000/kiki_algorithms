def lcm(l):
    i = 1
    while True:
        c = True
        for j in l:
            c = c and i % j == 0
        if c:
            break
        i += 1
    return i


def a(l):
    i = 1
    while True:
        c = True
        for j in range(len(l)):
            c = c and (i + j + 1) % l[j] == 0
        if c:
            break
        i += 1
    b = lcm(l)
    return ", ".join(map(str, [i + b * j for j in range(50)]))


print(a([8, 5, 9, 7]))
