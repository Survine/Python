class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None    
        
    def insert_at_beginning(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node  
        else:
            node.next = self.head  
            self.head = node  
            
    def insert_at_end(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node  
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
    
    def print_list(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            current = self.head
            while current:
                print(current.data, end=" -> ")
                current = current.next
            print("None")  


ll = LinkedList()
ll.insert_at_beginning(10)
ll.insert_at_beginning(20)
ll.insert_at_beginning(30)
ll.insert_at_end(40)
ll.insert_at_end(50)

ll.print_list()  