class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.end = None
        self.size = 0

    def is_empty(self):
        return self.front is None

    def enqueue(self, item):
        node = Node(item)
        if self.is_empty():
            self.front = node
            self.end = node
        else:
            self.end.next = new_node
            self.end = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            print("err: empty queue")
            return None
        data = self.front.data
        self.front = self.front.next
        if self.is_empty():
            self.end = None
        self.size -= 1
        return data

    def front(self):
        if self.is_empty():
            print("err: empty queue")
            return None
        return self.front.data

    def __len__(self):
        return self.size