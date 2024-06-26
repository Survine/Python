
print("Enter 'f' or 'F' to convert Celsius to Fahrenheit")
print("Enter 'c' or 'C' to convert Fahrenheit to Celsius")
choice = input("What do you want to convert: ")

if choice.lower() == 'f':
    celcius = float(input("Enter the temperature in Celsius: "))
    print(f"The {celcius} C will be {celcius * 1.8 + 32} F")
elif choice.lower() == 'c':
    farenheit = float(input("Enter the temperature in Fahrenheit: "))
    print(f"The {farenheit} F will be {(farenheit - 32) / 1.8} C")
else:
    print("Invalid choice")