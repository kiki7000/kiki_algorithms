input()
a = list(map(int, input().split()))
b = sorted(set(a))
c = {b[i]: i for i in range(len(b))}

list(map(lambda x: print(x, end=" "), [c[i] for i in a]))
