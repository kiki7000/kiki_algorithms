for i in range(int(input())):
    a = int(input())
    print("#" * a)
    for _ in range(max(a - 2, 0)):
        print("#" + "J" * (a - 2) + "#")
    print("#" * a + "\n" if a != 1 else "")
