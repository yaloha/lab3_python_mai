def bubble_sort(a: list[int]) -> list[int]:
    for i in range(len(a)):
        for j in range(len(a) - i - 1):
            if a[j] < a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a