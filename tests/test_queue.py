import pytest
from src.queue import (Node, Queue)


class TestBaseQueue:
    def test_queue_initialization_plus_is_empty(self):
        q = Queue()
        assert q.is_empty() == True
        assert len(q) == 0

    def test_enqueue_dequeue(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        assert q.dequeue() == 1
        assert q.dequeue() == 2
        assert q.dequeue() is None

    def test_size_after_operations(self):
        q = Queue()
        q.enqueue(10)
        q.enqueue(20)
        assert len(q) == 2
        q.dequeue()
        assert len(q) == 1

    def test_front(self):
        q = Queue()
        assert q.front() is None
        q.enqueue(1)
        assert q.front() == 1
        q.enqueue(2)
        assert q.front() == 1
        q.dequeue()
        assert q.front() == 2