class Stack():
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def get_stack(self):
        return self.items
    def is_empty(self):
        return self.items == []
    def peek(self):
        if not self.is_empty():
            return self.items[-1]

s = Stack()
s.is_empty()
s.push("A")
s.push("B")
# print(s.get_stack())
s.push("X")
print(s.get_stack())
print(s.peek())
s.pop()
print(s.peek())