from sys import stdin, stdout

arr = [0] * 10001

for _ in range(int(input())):
    arr[int(stdin.readline())] += 1

for i in range(len(arr)):
    if arr[i] == 0:
        continue

    for _ in range(arr[i]):
        stdout.write(f"{i}\n")
