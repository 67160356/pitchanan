class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop() if self.items else "Stack is empty!"
    def peek(self):
        return self.items[-1] if self.items else None
    def is_empty(self):
        return not self.items
    def size(self):
        return len(self.items)

s = Stack()
print(f"Is empty? {s.is_empty()}")
[s.push(i) for i in range(1, 6)]
print(f"Size after push: {s.size()}\nTop element: {s.peek()}")
[print(f"Pop: {s.pop()}") for _ in range(6)]
print(f"Is empty? {s.is_empty()}")