a = int(input())
print(sum([sum([i + j for j in range(i, a + 1)]) for i in range(0, a + 1)]))
