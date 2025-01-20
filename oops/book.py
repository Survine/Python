class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def display(self):
        print(f"{self.title} written by {self.author}")
        
x = Book("Do Epic Shit","Ankur Warikoo")
x.display()