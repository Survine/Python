# Covert Farenheight to Celsius and Vice versa

print("Enter 'f' or 'F' to convert Celsius to Fahrenheit")
print("Enter 'c' or 'C' to convert Fahrenheit to Celsius")
choice = input("What do you want to convert: ")

if choice == 'f' or choice == 'F':
    cel = float(input("Enter the temperature in Celsius: "))
    print(f"The {cel} C will be {cel * 1.8 + 32} F")
elif choice == 'c' or choice == 'C':
    far = float(input("Enter the temperature in Fahrenheit: "))
    print(f"The {far} F will be {(far - 32) / 1.8} C")
else:
    print("Invalid choice. Please enter 'f' or 'F' for Celsius to Fahrenheit, or 'c' or 'C' for Fahrenheit to Celsius.")
