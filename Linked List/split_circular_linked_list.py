class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def mid_point(self):
        if self.head is None:
            return None
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        mid = count/2
    def split(self):
        if int(self.mid) % 2 == 0:
            while self.mid:
                current = current.next
                print(current.data)
        else:
            