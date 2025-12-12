import math

def radix_sort(a: list[int], base: int = 10) -> list[int]:
    """Поразрядная сортировка"""
    if len(a) <= 1:
        return a
    k = int(math.log(max(a), base)) + 1
    if min(a) < 0:
        raise ValueError("nums should be >= 0")
    for i in range(k):
        temp_list = [[] for m in range(base)]
        for j in a:
            temp_list[(j // base ** i) % base].append(j)
        a = [n for temp in temp_list for n in temp]
    return a

