celsius_to_fahrenheit = lambda c: (c * 9/5) + 32

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = celsius_to_fahrenheit(celsius)

print(f"Temperature in Fahrenheit: {fahrenheit}")
print("Below freezing point" if fahrenheit < 32 else "Above freezing point")
