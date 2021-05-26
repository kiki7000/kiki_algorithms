a = int(input())
r = 0

for i in range(1, a + 1):
    if a == sum(map(int, str(i))) + i:
        r = i
        break

print(r)
