class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display(self):
        print(f"{self.brand}\n{self.model}\n{self.year}")
    
x = Car("Toyota", "Corolla", 2015)
x.display()