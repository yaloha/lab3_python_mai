import pytest
import math
from typing import List
from src.test_case_generators import (rand_int_array, rand_float_array)
from src.sort_algorithms import (bubble_sort, bucket_sort, counting_sort, heap_sort, quick_sort, radix_sort)

class TestBubbleSort:
    def test_bubble_sort_random(self):
        for i in range(10):
            a = rand_int_array(50, 1, 100)
            expected = sorted(a, reverse=True)
            result = bubble_sort(a)
            assert result == expected

    def test_bubble_sort_empty(self):
        a = []
        result = bubble_sort(a)
        assert result == []

    def test_bubble_sort_single(self):
        a = [33]
        result = bubble_sort(a)
        assert result == [33]


class TestBucketSort:
    def test_bucket_sort_random(self):
        for i in range(10):
            a = rand_float_array(100, 0.0, 100.0)
            result = bucket_sort(a)
            expected = sorted(a)
            assert result == expected

    def test_bucket_sort_not_default_buckets(self):
        a = rand_float_array(100, 0.0, 100.0)
        for buckets in [1, 5, 20, 100]:
            result = bucket_sort(a, buckets=buckets)
            expected = sorted(a)
            assert result == expected

    def test_bucket_sort_empty(self):
        a = []
        result = bucket_sort(a)
        assert result == []

    def test_bucket_sort_single(self):
        a = [3.3]
        result = bucket_sort(a)
        assert result == [3.3]


class TestCountingSort:
    def test_counting_sort_random(self):
        for i in range(10):
            a = rand_int_array(50, 0, 50)
            expected = sorted(a)
            result = counting_sort(a)
            assert result == expected

    def test_counting_sort_empty(self):
        a = []
        result = counting_sort(a)
        assert result == []

    def test_counting_sort_single(self):
        a = [7]
        result = counting_sort(a)
        assert result == [7]

    def test_counting_sort_err(self):
        a = [-1, 2, 3]
        with pytest.raises(ValueError, match="nums should be >= 0"):
            counting_sort(a)


class TestHeapSort:
    def test_heap_sort_random(self):
        for i in range(10):
            a = rand_int_array(50, -100, 100)
            expected = sorted(a)
            result = heap_sort(a)
            assert result == expected

    def test_heap_sort_empty(self):
        a = []
        result = heap_sort(a)

    def test_heap_sort_single(self):
        a = [33]
        result = heap_sort(a)
        assert result == [33]

    def test_heap_sort_negative(self):
        a = rand_int_array(20, -50, 50)
        result = heap_sort(a)
        expected = sorted(a)
        assert result == expected


class TestQuickSort:
    def test_quick_sort_random(self):
        for i in range(10):
            a = rand_int_array(50, -100, 100)
            expected = sorted(a)
            result = quick_sort(a, 0, len(a) - 1)
            assert result == expected

    def test_quick_sort_empty(self):
        a = []
        result = quick_sort(a, 0, -1)
        assert result == []

    def test_quick_sort_single(self):
        a = [33]
        result = quick_sort(a, 0, 0)
        assert result == [33]


class TestRadixSort:
    def test_radix_sort_random_non_negative(self):
        for i in range(10):
            a = rand_int_array(50, 0, 1000)
            expected = sorted(a)
            result = radix_sort(a)
            assert result == expected

    def test_radix_sort_empty(self):
        a = []
        result = radix_sort(a)
        assert result == []

    def test_radix_sort_single(self):
        a = [7]
        result = radix_sort(a)
        assert result == [7]

    def test_radix_sort_diff_base(self):
        a = rand_int_array(20, 0, 10000)
        for base in [2, 9, 16, 57]:
            result = radix_sort(a, base=base)
            expected = sorted(a)
            assert result == expected

    def test_radix_sort_err(self):
        a = [-1, 2, 3]
        with pytest.raises(ValueError, match="nums should be >= 0"):
            radix_sort(a)