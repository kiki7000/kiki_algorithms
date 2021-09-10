a = [False, False] + [i for i in range(2, 1000001)]
for i in range(2, 1000001):
    if not a[i]:
        continue
    for j in range(i * 2, 1000001, i):
        a[j] = False

while (b := int(input())) :
    c = 2
    while c * 2 <= b:
        if a[c] and a[b - c]:
            break
        c += 1

    if c * 2 > b:
        print("Goldbach's conjecture is wrong.")
    else:
        print(f"{b} = {c} + {b - c}")
