# Find if the user is eligible to get a discount of 10%

cost = float(input("Enter the total cost of items purchased :"))
if cost < 1000:
    print(f"You are not eligible for a discount of 10% for the cost of {cost}.")
else:
    print(f"You are eligible to get a discount of 10% for the cost of {cost}")
    price = cost - (10/100)*cost
    print(f"Your discounted price is {price}")
