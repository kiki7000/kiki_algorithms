for _ in range(int(input())):
    s = 0
    sc = 0

    for i in input():
        if i == "O":
            sc += 1
            s += sc
        else:
            sc = 0

    print(s)
