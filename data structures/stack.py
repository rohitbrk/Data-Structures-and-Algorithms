from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, element):
        self.container.append(element)

    def pop(self):
        self.container.pop()

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

    def peek(self):
        return self.container[-1]


if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    print(s.peek())
    s.push(3)
    s.pop()
    s.pop()
    print(s.is_empty())
    print(s.size())
    s.pop()
    print(s.is_empty())
