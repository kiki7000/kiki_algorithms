for _ in range(int(input())):
    a = list(map(int, input().split()))
    print(
        2 * (a[3] + a[7]) + max(a[0] + a[4], 1) + max(a[1] + a[5], 1) * 5 + max(a[2] + a[6], 0) * 2
    )
