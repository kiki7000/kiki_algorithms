a = int(input())
print(1 if (not a % 400) or (a % 100 and not a % 4) else 0)
