def pivot_divide(a: list[int], first: int, last: int) -> int:
    """Функция для разбиения по опорному элементу"""
    pivot = a[last]
    i = first - 1
    for j in range(first, last):
        if a[j] < pivot:
            i += 1
            a[j], a[i] = a[i], a[j]
    a[i + 1], a[last] = a[last], a[i + 1]
    return i + 1


def quick_sort(a: list[int], first: int, last: int) -> list[int]:
    """Быстрая сортировка"""
    if first < last:
        pivot = pivot_divide(a, first, last)
        quick_sort(a, first, pivot - 1)
        quick_sort(a, pivot + 1, last)
    return a