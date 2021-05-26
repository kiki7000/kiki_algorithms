for _ in range(int(input())):
    a = list(map(int, input().split()))
    s = sum(a[1:]) // a[0]

    print(f"{round(len(list(filter(lambda x: x > s, a[1:]))) / a[0] * 100, 3):.3f}%")
