c, k, p = map(int, input().split())
a = (c + 1) * c // 2
print(k * a + p * (a * (2 * c + 1) // 3))
