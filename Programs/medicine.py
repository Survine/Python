class Medicine:
    def __init__(self, name, price, mfd, exp, power, quantity):
        self.name = name
        self.price = price
        self.mfd = mfd
        self.exp = exp
        self.power = power
        self.quantity = quantity

class User:
    def __init__(self, name, age, address, gender, phone):
        self.name = name
        self.age = age
        self.address = address
        self.gender = gender
        self.phone = phone

class BillingSystem:
    def generate_invoice(self, user, purchase_date, medicine):
        billing_cost = medicine.price * medicine.quantity
        print("Invoice:")
        print("Purchasing Date:", purchase_date)
        print("Customer Details:")
        print("Name:", user.name)
        print("Address:", user.address)
        print("Gender:", user.gender)
        print("Phone:", user.phone)
        print("\nMedicines:")
        print(f"{medicine.name}\nQuantity: {medicine.quantity}\nPrice per unit: ${medicine.price}")
        print(f"Billing Cost: ${billing_cost}")

paracetamol = Medicine("Paracetamol", 255, "2023-01-01", "2025-01-01", "500mg", 5)
user1 = User("Hriday", 19, "Agartala", "Male", 6009416189)

billing_system = BillingSystem()
billing_system.generate_invoice(user1, "2024-04-04", paracetamol)
