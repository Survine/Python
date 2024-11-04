a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
sum = a + b
if sum % 2 == 0:
    print(f"The sum of {a} and {b} is {sum} and it is an even number")
else:
    print(f"The sum of {a} and {b} is {sum} and it is an odd number")