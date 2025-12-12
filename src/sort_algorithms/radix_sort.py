def radix_sort(a: list[int], base: int = 10) -> list[int]:
    k = len(str(max(a)))
    for i in range(k):
        temp_list = [[] for _ in range(base)]
        for j in a:
            temp_list[(j // base ** i) % base].append(j)
        a = [n for temp in temp_list for n in temp]
    return a

