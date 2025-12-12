import pytest
from src.factorial_fibonachi import (factorial, factorial_recursive, fibo_recursive, fibo)


class TestFactorials:
    def test_factorial_positive(self):
        assert factorial(5) == 120
        assert factorial(3) == 6


    def test_factorial_zero(self):
        result = factorial(0)
        assert result == 1


    def test_factorial_negative(self):
        with pytest.raises(ValueError):
            factorial(-1)


    def test_factorial_recursive_positive(self):
        assert factorial_recursive(5) == 120
        assert factorial_recursive(3) == 6


    def test_factorial_recursive_zero(self):
        result = factorial_recursive(0)
        assert result == 1


    def test_factorial_recursive_negative(self):
        with pytest.raises(ValueError):
            factorial_recursive(-5)


class TestFibo:
    def test_fibo_positive(self):
        assert fibo(6) == 8
        assert fibo(10) == 55


    def test_fibo_zero(self):
        assert fibo(0) == 0


    def test_fibo_negative(self):
        with pytest.raises(ValueError):
            fibo(-1)

    def test_fibo_recursive_positive(self):
        assert fibo_recursive(6) == 8
        assert fibo_recursive(10) == 55  


    def test_fibo_recursive_zero(self):
        assert fibo_recursive(0) == 0 


    def test_fibo_recursive_negative(self):
        with pytest.raises(ValueError):
            fibo_recursive(-3)
            