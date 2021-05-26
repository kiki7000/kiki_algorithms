r = [True for _ in range(10001)]
for i in range(1, 10001):
    a = i + sum(map(int, list(str(i))))
    if a <= 10000:
        r[a] = False

for i in range(1, len(r)):
    if r[i]:
        print(i)
