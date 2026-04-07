class Node:
    def __init__(self, value=0, next_node=None):
        self.value = value
        self.next = next_node

class Stack:
    def __init__(self):
        self.head = None

    def push(self, x: int) -> None:
        new_node = Node(x, self.head)
        self.head = new_node

    def pop(self) -> int:
        if self.is_empty():
            return None
        popped_value = self.head.value
        self.head = self.head.next
        return popped_value

    def peek(self) -> int:
        if self.is_empty():
            return None
        return self.head.value

    def is_empty(self):
        return self.head is None

class MyQueue:
    def __init__(self):
        self.stack_in = Stack()
        self.stack_out = Stack()

    def push(self, x: int) -> None:
        self.stack_in.push(x)

    def transfer(self):
        if self.stack_out.is_empty():
            while not self.stack_in.is_empty():
                self.stack_out.push(self.stack_in.pop())

    def pop(self) -> int:
        self.transfer()
        return self.stack_out.pop()

    def peek(self) -> int:
        self.transfer()
        return self.stack_out.peek()

    def empty(self) -> bool:
        return self.stack_in.is_empty() and self.stack_out.is_empty()


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
