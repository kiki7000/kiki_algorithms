a, rank = [], []
for _ in range(int(input())):
    a.append(list(map(int, input().split())))
    rank.append(1)

for i in range(len(a)):
    for j in range(len(a)):
        if a[i][0] < a[j][0] and a[i][1] < a[j][1]:
            rank[i] += 1

for i in range(len(a)):
    print(rank[i], end=" ")
