a, b = map(int, input().split())
print(" ".join(map(lambda k: str(k - a * b), map(int, input().split()))))
