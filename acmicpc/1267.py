input()
a = list(map(int, input().split()))
b, c = sum([i // 30 + 1 for i in a]) * 10, sum([i // 60 + 1 for i in a]) * 15

if b == c:
    print(f"Y M {b}")
elif b < c:
    print(f"Y {b}")
else:
    print(f"M {c}")
