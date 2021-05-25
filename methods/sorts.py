from random import shuffle
from math import log

from asyncio import sleep, wait, run

from typing import Callable, List

from .utils import (
    is_sorted, default_compare, reverse_default_compare,
    get_digit
)

def bubble_sort(l: List[int], check_sort: bool = False, key: Callable = lambda x: x, compare: Callable = default_compare) -> List[int]:
    """
    시간복잡도: O(n²)
    """

    if len(l) < 2: return l
    if check_sort and is_sorted(l, key = key, compare = compare): return l
    edit_l = list(map(key, l))

    for i in range(len(l) - 1):
        for j in range(len(l) - 1 - i):
            if not compare(edit_l[j], edit_l[j + 1]):
                edit_l[j], edit_l[j + 1] = edit_l[j + 1], edit_l[j]
                l[j], l[j + 1] = l[j + 1], l[j]
    return l    

def selection_sort(l: List[int], check_sort: bool = False, key: Callable = lambda x: x, compare: Callable = default_compare) -> List[int]:
    """
    시간복잡도: O(n²)
    """

    if len(l) < 2: return l
    if check_sort and is_sorted(l, key = key, compare = compare): return l
    edit_l = list(map(key, l))

    for i in range(len(l) - 1):
        m = i
        for j in range(i + 1, len(l)):
            if not compare(edit_l[m], edit_l[j]): m = j
        
        if m != i:
            edit_l[i], edit_l[m] = edit_l[m], edit_l[i]
            l[i], l[m] = l[m], l[i]

    return l    

def insertion_sort(l: List[int], check_sort: bool = False, key: Callable = lambda x: x, compare: Callable = default_compare) -> List[int]: 
    """
    시간복잡도: O(n²)
    """
    
    if len(l) < 2: return l
    if check_sort and is_sorted(l, key = key, compare = compare): return l
    edit_l = list(map(key, l))

    for i in range(1, len(l)):
        j = i - 1
        k = edit_l[i]
        while not compare(edit_l[j], k) and j >= 0:
            edit_l[j + 1] = edit_l[j]
            l[j + 1] = l[j]
            j -= 1
        edit_l[j + 1] = k
        l[j + 1] = k
    return l    

def merge(l, r, key: Callable = lambda x: x, compare: Callable = default_compare) -> List[int]:
    res = []
    el = list(map(key, l))
    er = list(map(key, r))
    while len(l) or len(r):
        if len(l) and len(r):
            if compare(el[0], er[0]): 
                res.append(l[0])
                l = l[1:]
                el = el[1:]
            else:
                res.append(r[0])
                r = r[1:]
                er = er[1:]
        elif len(l):
            res.append(l[0])
            l = l[1:]
            el = el[1:]
        elif len(r):
            res.append(r[0])
            r = r[1:]
            er = er[1:]
    return res


def merge_sort(l: List[int], check_sort: bool = False, key: Callable = lambda x: x, compare: Callable = default_compare) -> List[int]: 
    """
    시간복잡도: O(n log n)
    """

    if len(l) < 2: return l
    if check_sort and is_sorted(l, key = key, compare = compare): return l
    lft = l[:len(l) // 2]
    rgt = l[len(l) // 2:]
    return merge(merge_sort(lft, check_sort = check_sort, key = key, compare = compare), merge_sort(rgt, check_sort = check_sort, key = key, compare = compare), key = key, compare = compare)

def heapify(l: List[int], s: int, i: int, key: Callable = lambda x: x, compare: Callable = default_compare) -> List[int]:
    edit_l = list(map(key, l))
    lr = i
    lft = 2 * lr + 1
    rgt = 2 * lr + 2
    if lft < s and compare(edit_l[i], edit_l[lft]): lr = lft
    if rgt < s and compare(edit_l[lr], edit_l[rgt]): lr = rgt
    if lr != i:
        l[i], l[lr] = l[lr], l[i]
        l = heapify(l, s, lr, key, compare)
    return l

def heap_sort(l: List[int], check_sort: bool = False, key: Callable = lambda x: x, compare: Callable = default_compare) -> List[int]:
    """
    시간복잡도: O(n log n)
    """

    if len(l) < 2: return l
    if check_sort and is_sorted(l, key = key, compare = compare): return l
    for i in range(len(l), -1, -1): l = heapify(l, len(l), i, key = key, compare = compare)
    for i in range(len(l) - 1, 0, -1):
        l[i], l[0] = l[0], l[i]
        l = heapify(l, i, 0, key = key, compare = compare)
    return l

def quick_sort(l: List[int], check_sort: bool = False, key: Callable = lambda x: x, compare: Callable = default_compare, compare2: Callable = reverse_default_compare) -> List[int]:
    """
    시간복잡도: O(n log n)
    """

    if len(l) < 2: return l
    if check_sort and is_sorted(l, key = key, compare = compare): return l
    edit_l = list(map(key, l))
    pv = edit_l[len(l) // 2]
    a, b, c, = [], [], []

    for i in range(0, len(l)):
        if compare(edit_l[i], pv): a.append(l[i])   
        elif compare2(edit_l[i], pv): c.append(l[i])
        else: b.append(l[i])

    return quick_sort(a, check_sort = check_sort, key = key, compare = compare, compare2 = compare2) + b + quick_sort(c, check_sort = check_sort, key = key, compare = compare, compare2 = compare2)

def tim_sort(l: List[int], check_sort: bool = False, key: Callable = lambda x: x) -> List[int]:
    """
    (Python 내장 정렬 함수)
    """

    if len(l) < 2: return l
    if check_sort and is_sorted(l, key = key): return l
    return sorted(l, key = key)

def random_sort(l: List[int], check_sort: bool = False, key: Callable = lambda x: x, compare: Callable = default_compare) -> List[int]:
    """
    시간복잡도: O(n×n!)
    """

    if len(l) < 2: return l
    if check_sort and is_sorted(l, key = key, compare = compare): return l
    while True:
        shuffle(l)
        if is_sorted(l, key = key, compare = compare): return l
    
def double_random_sort(l: List[int], check_sort: bool = False, key: Callable = lambda x: x, compare: Callable = default_compare) -> List[int]:
    """
    시간복잡도: O(n!^n!)
    """

    if len(l) < 2: return l
    if check_sort and is_sorted(l, key = key, compare = compare): return l
    i = 2
    while True:
        l[:i] = random_sort(l[:i])
        i += 1
        if not is_sorted(l[:i]):
            shuffle(l)
            i = 2
        if is_sorted(l, key = key, compare = compare): return l

def counting_sort(l: List[int], check_sort: bool = False):
    """
    시간복잡도: O(n + k)
    """

    if len(l) < 2: return l
    if check_sort and is_sorted(l): return l
    l = list(map(int, l))
    res = [-1] * len(l)
    a = [0] * (max(l) + 1)
    for i in l: a[i] += 1
    for i in range(max(l)): a[i + 1] += a[i]
    for i in reversed(l):
        res[a[i] - 1] = i
        a[i] -= 1
    return res

def counting_sort_with_digits(l: List[int], d: int, b: int = 10):
    l = list(map(int, l))
    res = [-1] * len(l)
    a = [0] * b
    for i in l: a[get_digit(i, d, b)] += 1
    for i in range(b - 1): a[i + 1] += a[i]
    for i in reversed(l):
        res[a[get_digit(i, d, b)] - 1] = i
        a[get_digit(i, d, b)] -= 1
    return res

def radix_sort(l: List[int], b: int = 10, check_sort: bool = False):
    """
    시간복잡도: O(kn)
    """

    if len(l) < 2: return l
    if check_sort and is_sorted(l): return l
    l = list(map(int, l))
    ds = int(log(max(l), b) + 1)
    for d in range(ds): l = counting_sort_with_digits(l, d, b)
    return l

def shell_sort(l: List[int], check_sort: bool = False):
    """
    시간복잡도: O(n²)
    """

    if len(l) < 2: return l
    if check_sort and is_sorted(l): return l
    l = list(map(int, l))
    g = len(l) // 2
    while g > 0:
        for s in range(g): l = gapinsertion_sort(l, s, g)
        g //= 2
    return l

def gapinsertion_sort(l: List[int], s, g):
    for i in range(s + g, len(l), g):
        v = l[i]
        p = i

        while p >= g and l[p - g] > v:
            l[p] = l[p - g]
            p -= g

        l[p] = v
    
    return l

def sleep_sort(l: List[int], check_sort: bool = False, minify = 10000000000):
    """
    시간복잡도: O(kn)
    """

    if len(l) < 2: return l
    if check_sort and is_sorted(l): return l
    l = list(map(int, l))
    res = []

    async def sleep_return(n):
        await sleep(n / minify)
        res.append(n)
    
    run(wait(map(sleep_return, l)))
    return res

def cocktail_sort(l: List[int], check_sort: bool = False, key: Callable = lambda x: x, compare: Callable = default_compare) -> List[int]: 
    if len(l) < 2: return l
    if check_sort and is_sorted(l, key = key, compare = compare): return l
    edit_l = list(map(key, l))

    sw = True
    s = 0
    e = len(l) - 1
    while sw:
        sw = False
        for i in range(s, e):
            if not compare(edit_l[i], edit_l[i + 1]):
                edit_l[i], edit_l[i + 1] = edit_l[i + 1], edit_l[i]
                l[i], l[i + 1] = l[i + 1], l[i]
                sw = True
        
        if not sw: return l
        sw = False
        e -= 1

        for i in range(e - 1, s - 1, -1):
            if not compare(edit_l[i], edit_l[i + 1]):
                edit_l[i], edit_l[i + 1] = edit_l[i + 1], edit_l[i]
                l[i], l[i + 1] = l[i + 1], l[i]
                sw = True
        s += 1
    
    return l

def gnome_sort(l: List[int], check_sort: bool = False, key: Callable = lambda x: x, compare: Callable = default_compare) -> List[int]: 
    if len(l) < 2: return l
    if check_sort and is_sorted(l, key = key, compare = compare): return l
    edit_l = list(map(key, l))
    i = 0
    while i < len(l):
        if not i: i += 1
        if not compare(edit_l[i], edit_l[i - 1]): i += 1
        else: 
            l[i], l[i - 1] = l[i - 1], l[i]
            edit_l[i], edit_l[i - 1] = edit_l[i - 1], edit_l[i]
            i -= 1
    return l

def comb_sort(l: List[int], check_sort: bool = False, key: Callable = lambda x: x, compare: Callable = default_compare) -> List[int]:
    """
    시간복잡도: O(n²)
    """

    if len(l) < 2: return l
    if check_sort and is_sorted(l, key = key, compare = compare): return l
    edit_l = list(map(key, l))
    g = len(l)
    sw = True
    while g != 1 or sw:
        g = g * 10 // 13
        if g < 1: g = 1
        sw = False
        for i in range(0, len(l) - g):
            if not compare(edit_l[i], edit_l[i + g]):
                l[i], l[i + g] = l[i + g], l[i]
                edit_l[i], edit_l[i + g] = edit_l[i + g], edit_l[i]
                sw = True
    return l

def pigeonhole_sort(l: List[int], check_sort: bool = False) -> List[int]: 
    if len(l) < 2: return l
    if check_sort and is_sorted(l): return l
    
    a = min(l)
    h = [0] * (max(l) - a + 1)
    for i in l: h[i - a] += 1
    
    i = 0
    for c in range(max(l) - a + 1):
        while h[c]:
            h[c] -= 1
            l[i] = i + a
            i += 1

    return l

def brick_sort(l: List[int], check_sort: bool = False, key: Callable = lambda x: x, compare: Callable = default_compare) -> List[int]: 
    if len(l) < 2: return l
    if check_sort and is_sorted(l, key = key, compare = compare): return l
    edit_l = list(map(key, l))
    sw = True

    while sw:
        sw = False
        
        for i in range(1, len(l) - 1, 2):
            if not compare(edit_l[i], edit_l[i + 1]):
                edit_l[i], edit_l[i + 1] = edit_l[i + 1], edit_l[i]
                l[i], l[i + 1] = l[i + 1], l[i]
                sw = True

        for i in range(0, len(l) - 1, 2):
            if not compare(edit_l[i], edit_l[i + 1]):
                edit_l[i], edit_l[i + 1] = edit_l[i + 1], edit_l[i]
                l[i], l[i + 1] = l[i + 1], l[i]
                sw = True

    return l