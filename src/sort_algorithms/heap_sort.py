def create_heap(a: list[int], n: int, i: int) -> list[int]:
    """Функция для создания бинарной кучи из передаваемого массивва"""
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and a[l] > a[largest]:
        largest = l
    if r < n and a[r] > a[largest]:
        largest = r
    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        create_heap(a, n, largest)



def heap_sort(a: list[int]) -> list[int]:
    """Функция для сортировки кучей"""
    n = len(a)
    for i in range(n // 2 - 1, -1, -1):
        create_heap(a, n, i)
        
    for i in range(n - 1, 0, -1):
        a[0], a[i] = a[i], a[0]
        create_heap(a, i, 0)
    return a