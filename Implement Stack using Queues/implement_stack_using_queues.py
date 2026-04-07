class Node:
    def __init__(self, value=0, next_node=None):
        self.value = value
        self.next = next_node

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def push(self, val):
        new_node = Node(val)
        if self.tail:
            self.tail.next = new_node
        self.tail = new_node
        if not self.head:
            self.head = new_node
        self._size += 1

    def pop(self):
        if self.is_empty():
            return None
        popped_value = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self._size -= 1
        return popped_value

    def peek(self):
        if self.is_empty():
            return None
        return self.head.value

    def is_empty(self):
        return self.head is None

    def size(self):
        return self._size

class MyStack:
    def __init__(self):
        self.q = Queue()

    def push(self, x: int) -> None:
        self.q.push(x)
        for _ in range(self.q.size() - 1):
            self.q.push(self.q.pop())

    def pop(self) -> int:
        return self.q.pop()

    def top(self) -> int:
        return self.q.peek()

    def empty(self) -> bool:
        return self.q.is_empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
