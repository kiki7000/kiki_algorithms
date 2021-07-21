from bisect import bisect_left

input()
a = list(map(int, input().split()))
b = []


for i in a:
    if len(b) == 0 or b[-1] < i:
        b.append(i)
    else:
        b[bisect_left(b, i)] = i

print(len(b))
