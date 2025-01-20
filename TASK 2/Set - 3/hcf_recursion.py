def HCF(a, b, n):
    while n > 0:
        if a % n == 0 and b % n == 0:
            return n
        else:
            return HCF(a, b, n - 1)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(f"HCF of {num1} and {num2} is {HCF(num1, num2, min(num1, num2))}")