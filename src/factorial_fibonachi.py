def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("number must be >= 1")
    res, i = 1, 2
    while i <= n:
        res *= i
        i += 1
    return res


def factorial_recursive(n: int) -> int:
    if n < 0:
        raise ValueError("number must be >= 1")
    elif n > 1:
        return n * factorial_recursive(n - 1)
    return n


def fibo(n: int) -> int:
    a, b = 0, 1
    while n > 0:
        if n % 2:
            a += b
        else:
            b += a
        n -= 1


def fibo_recursive(n: int) -> int:
    if n < 0:
        raise ValueError("number must be >= 1")
    elif n in {0, 1}:
        return n
    else:
        return fibo_recursive(n - 1) + fibo_recursive(n - 2)