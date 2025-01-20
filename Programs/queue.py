class Queue:
    
    def __init__(self):
        self.items = []
        
    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def __str__(self):
        return str(self.items)
    
#main
q = Queue()
q.enqueue(1)
print(q)
q.enqueue(2)
print(q)
print(q.dequeue())
print(q)