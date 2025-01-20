a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")
if operation == "+":
    print(f"The sum of {a} and {b} is {a + b}")
elif operation == "-":
    print(f"The difference of {a} and {b} is {a - b}")
elif operation == "*":
    print(f"The product of {a} and {b} is {a * b}")
elif operation == "/":
    print(f"The division of {a} and {b} is {a / b}")
else:
    print("Invalid operation")