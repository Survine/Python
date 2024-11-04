# Swapping Variables using a third variable and without using a third variable

a = input("Enter something: ")
b = input("Enter something more: ")
print("Before swapping:", a, b)

# Using a third variable to swap
temp = a
a = b
b = temp
print("After swapping with third variable:", a, b)

# Swapping back without using a third variable
a, b = b, a
print("After swapping back without third variable:", a, b)
