from .ext import is_sorted, default_compare, reverse_default_compare, get_digit
from random import shuffle
from math import log

def bubble_sort(l: list, check_sort: bool = False, key = lambda x: x, compare = default_compare) -> list: 
    if len(l) < 2: return l
    if check_sort and is_sorted(l, key = key, compare = compare): return l
    edit_l = list(map(key, l))

    for i in range(len(l) - 1):
        for j in range(len(l) - 1 - i):
            if not compare(edit_l[j], edit_l[j + 1]):
                edit_l[j], edit_l[j + 1] = edit_l[j + 1], edit_l[j]
                l[j], l[j + 1] = l[j + 1], l[j]
    return l    

def selection_sort(l: list, check_sort: bool = False, key = lambda x: x, compare = default_compare) -> list: 
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

def insertion_sort(l: list, check_sort: bool = False, key = lambda x: x, compare = default_compare) -> list: 
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

def merge(l, r, key = lambda x: x, compare = default_compare) -> list:
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


def merge_sort(l: list, check_sort: bool = False, key = lambda x: x, compare = default_compare) -> list: 
    if len(l) < 2: return l
    if check_sort and is_sorted(l, key = key, compare = compare): return l
    lft = l[:len(l) // 2]
    rgt = l[len(l) // 2:]
    return merge(merge_sort(lft, check_sort = check_sort, key = key, compare = compare), merge_sort(rgt, check_sort = check_sort, key = key, compare = compare), key = key, compare = compare)

def heapify(l: list, s: int, i: int, key = lambda x: x, compare = default_compare) -> list:
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

def heap_sort(l: list, check_sort: bool = False, key = lambda x: x, compare = default_compare) -> list: 
    if len(l) < 2: return l
    if check_sort and is_sorted(l, key = key, compare = compare): return l
    for i in range(len(l), -1, -1): l = heapify(l, len(l), i, key = key, compare = compare)
    for i in range(len(l) - 1, 0, -1):
        l[i], l[0] = l[0], l[i]
        l = heapify(l, i, 0, key = key, compare = compare)
    return l

def quick_sort(l: list, check_sort: bool = False, key = lambda x: x, compare = default_compare, compare2 = reverse_default_compare) -> list: 
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

def tim_sort(l: list, check_sort: bool = False, key = lambda x: x) -> list: 
    if len(l) < 2: return l
    if check_sort and is_sorted(l, key = key): return l
    return sorted(l, key = key)

def random_sort(l: list, check_sort: bool = False, key = lambda x: x, compare = default_compare) -> list:
    if len(l) < 2: return l
    if check_sort and is_sorted(l, key = key, compare = compare): return l
    while True:
        shuffle(l)
        if is_sorted(l, key = key, compare = compare): return l

def counting_sort(l: list, check_sort: bool = False):
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

def counting_sort_with_digits(l: list, d: int, b: int = 10):
    l = list(map(int, l))
    res = [-1] * len(l)
    a = [0] * b
    for i in l: a[get_digit(i, d, b)] += 1
    for i in range(b - 1): a[i + 1] += a[i]
    for i in reversed(l):
        res[a[get_digit(i, d, b)] - 1] = i
        a[get_digit(i, d, b)] -= 1
    return res

def radix_sort(l, b: int = 10, check_sort: bool = False):
    if len(l) < 2: return l
    if check_sort and is_sorted(l): return l
    l = list(map(int, l))
    ds = int(log(max(l), b) + 1)
    for d in range(ds): l = counting_sort_with_digits(l, d, b)
    return l
