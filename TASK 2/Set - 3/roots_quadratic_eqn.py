import math

a = 1
b = -3
c = 2

# Calculate the discriminant
discriminant = b**2 - 4*a*c

# Determine the nature of the roots
if discriminant > 0:
    nature = "real and distinct"
elif discriminant == 0:
    nature = "real and equal"
else:
    nature = "imaginary"

# Calculate the two roots
root1 = (-b + (discriminant)**0.5 / (2*a))
root2 = (-b - (discriminant)**0.5 / (2*a))

print(f"The roots are {root1} and {root2}, and they are {nature}.")
