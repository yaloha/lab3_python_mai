def counting_sort(a: list[int]) -> list[int] :
    mx = max(a)
    count_list = [0] * (mx + 1)
    for i in a:
        count_list[i] += 1
    j = 0
    for i in range(len(count_list)):
        k = count_list[i]
        while k > 0:
            a[j] = i
            k -= 1
            j += 1
    return a
