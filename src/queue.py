class Node:
    def __init__(self, data):
        """Функция для инициализации Node"""
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        """Функция для инициализации Queue"""
        self.begin = None
        self.end = None
        self.size = 0

    def is_empty(self):
        """Функция, проверяющая пустая ли очередь"""
        return self.begin is None

    def enqueue(self, item):
        """Функция, вставляющая элемент в очередь"""
        node = Node(item)
        if self.is_empty():
            self.begin = node
            self.end = node
        else:
            self.end.next = node
            self.end = node
        self.size += 1

    def dequeue(self):
        """Функция, вставляющая элемент из очереди"""
        if self.is_empty():
            print("err: empty queue")
            return None
        data = self.begin.data
        self.begin = self.begin.next
        if self.is_empty():
            self.end = None
        self.size -= 1
        return data

    def front(self):
        """Функция, просматривающая первый элемент в очереди"""
        if self.is_empty():
            print("err: empty queue")
            return None
        return self.begin.data

    def __len__(self):
        """Функция, возвращающая длинну очереди"""
        return self.size