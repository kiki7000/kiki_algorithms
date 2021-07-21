n, w, h = map(int, input().split())
a = (w ** 2 + h ** 2) ** 0.5
for _ in range(n):
    b = int(input())
    print("DA" if b <= a else "NE")
