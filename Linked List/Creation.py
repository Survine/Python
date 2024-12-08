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
    
    def delete_by_value(self, value):
        if self.head is None:
            print("The list is empty. Nothing to delete.")
            return
        
        if self.head.data == value:
            self.head = self.head.next
            print(f"Node with value {value} deleted.")
            return
        
        current = self.head
        while current.next and current.next.data != value:
            current = current.next
        
        if current.next is None:
            print(f"Node with value {value} not found.")
        else:
            current.next = current.next.next
            print(f"Node with value {value} deleted.")
    
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

print("Original list:")
ll.print_list()  

# Deleting nodes
ll.delete_by_value(30) 
ll.delete_by_value(10)  
ll.delete_by_value(60)  

print("\nUpdated list:")
ll.print_list()
