while (a := int(input())) :
    while len(str(a := sum(map(int, str(a))))) > 1:
        continue
    print(a)
