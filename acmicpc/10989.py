from sys import stdin

arr = [0] * 10001

for _ in range(int(input())):
    arr[int(stdin.readline())] += 1

for i in range(len(arr)):
    print(f"{i}\n" * arr[i], end="")
