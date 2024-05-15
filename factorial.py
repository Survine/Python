# Factorial using for loop
'''
n = int(input("Enter a number :"))
if n < 0:
    print("The factorial doesn't exist")
elif n == 0:
    print("The factorial is 1")
else:
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    print(fact)
'''


# Factorial using math library

import math
num = int(input("Enter a number :"))
p = math.factorial(num)
print(f"The Factorial of {num} is {p}")

