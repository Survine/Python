class Bill:
    def __init__(self):
        self.items = {}
        
    def add_item(self, item_name, price, quantity):
        self.items[item_name] = price * quantity
    
    def calculate_gst(self, gst_percent):
        for item in self.items:
            self.items[item] += (self.items[item] * gst_percent) / 100
    
    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
        else:
            print(f"Item {item_name} not found in the bill.")

    def print_bill(self):
        for i in range (50):
            print("-", end="")
        print("\n")
        print("Billing Details")
        print("\n")
        for item in self.items:
            print(item, ": ", self.items[item])
        total_items = len(self.items)
        print("Total: ", sum(self.items.values()))
        print(f"Total items: {total_items}")
        print("\n")
        for i in range (50):
            print("-", end="")

bill = Bill()

while True:
    item_name = input("Enter the item name: ")
    price = int(input("Enter the price of the item: "))
    quantity = int(input("Enter the quantity of the item: "))
    bill.add_item(item_name, price, quantity)
    choice = input("Do you want to add more items? (yes/no): ")
    if choice.lower() == "no":
        break
gst_percent = int(input("Enter the GST rate: "))
bill.calculate_gst(gst_percent)
bill.print_bill()
