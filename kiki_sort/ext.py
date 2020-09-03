def default_compare(a, b) -> bool: return a < b
def reverse_default_compare(a, b) -> bool: return a > b
def get_digit(n, d, b) -> int: return (n // b ** d) % b

def is_sorted(l, key = lambda x: x, compare = default_compare) -> bool:
    l = list(map(key, l))
    for i in range(1, len(l)): 
        res = compare(l[i - 1], l[i])
        if not res: return False
    return True