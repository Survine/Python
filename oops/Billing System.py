class Bill:
    def __init__(self, items):
        self.items = items
        self.total = 0
        self.gst = 0
        self.grand_total = 0

    def calculate_price(self):
        price = int(input("Enter the price of the item: "))
        quantity = int(input("Enter the quantity of the item: "))
        self.total = price * quantity
        
    def calculate_gst(self):
        gst_percent = int(input("Enter the GST rate: "))
        self.gst = (self.total * gst_percent) / 100
    
    def calculate_total(self):
        self.grand_total = self.total + self.gst
    
    def print_bill(self):
        print("Items: ", self.items)
        print("Original price: ", self.total)
        print("GST: ", self.gst)
        print("Grand Total: ", self.grand_total)
        
items = []
item_name = input("Enter the item name: ")
items.append(item_name)
bill = Bill(items)
bill.calculate_price()
bill.calculate_gst()
bill.calculate_total()
bill.print_bill()
