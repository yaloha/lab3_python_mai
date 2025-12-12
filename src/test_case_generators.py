import random

def rand_int_array(n: int, lo: int, hi: int, *, distinct=False, seed=None) -> list[int]:
    """Функция, генерирующая случайный массив чисел для тестов"""
    if seed is not None:
        random.seed(seed)
    if distinct:
        if hi - lo + 1 < n:
            raise ValueError(f"not enough numbers for uniques. [hi, lo] < n")
        return random.sample(range(lo, hi + 1), n)
    else:
        return [random.randint(lo, hi) for i in range(n)]


def nearly_sorted(n: int, swaps: int, *, seed=None) -> list[int]:
    """Функция, генерирующая случайный, близкий к отсортированному массиву чисел для тестов"""
    if seed is not None:
        random.seed(seed)
    a = sorted(list(random.randint(range(n), n)))
    for k in range(swaps):
        i, j = random.sample(range(n), 2)
        arr[i], arr[j] = arr[j], arr[i]
    return a


def many_duplicates(n: int, k_unique=5, *, seed=None) -> list[int]:
    """Функция, генерирующая случайный массив чисел с большим количеством повторяющихся чисел для тестов"""
    if seed is not None:
        random.seed(seed)
    if k_unique <= 0:
        k_unique = 1
    elif k_unique > n:
        k_unique = n
    unique_values = random.sample(range(-10 ** 9, 10 ** 9), k_unique)
    return [random.choice(unique_values) for i in range(n)]


def reverse_sorted(n: int) -> list[int]:
    """Функция, генерирующая массив, отсортированный в обратном порядке"""
    return list(range(n, 0, -1))


def rand_float_array(n: int, lo=0.0, hi=1.0, *, seed=None) -> list[float]:
    """Функция, генерирующая случайный массив чисел с плавающей точкой для тестов"""
    if seed is not None:
        random.seed(seed)
    return [random.uniform(lo, hi) for i in range(n)]