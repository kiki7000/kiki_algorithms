from typing import List, Callable


def compare(a: int, b: int) -> int:
    if a > b:
        return 1
    elif a == b:
        return 0
    elif a < b:
        return -1


def get_digit(n: int, d: int, b: int) -> int:
    return (n // b ** d) % b


def is_sorted(l: List[int], key: Callable = lambda x: x, compare: Callable = compare) -> bool:
    l = list(map(key, l))

    for i in range(1, len(l)):
        res = compare(l[i - 1], l[i])
        if compare(l[i - 1], l[i]) - 1:
            return False

    return True
