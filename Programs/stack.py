class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def __str__(self):
        return str(self.items)

#Main
s = Stack()
s.push(1)
s.push(2)
print(s)
print(s.pop())
print(s)