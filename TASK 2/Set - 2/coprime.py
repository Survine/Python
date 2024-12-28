def coPrime(a,b):
    for i in range(2, min(a,b)+1):
        if a%i==0 and b%i==0:
            return False
    return True

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if coPrime(a,b):
    print(f"{a} and {b} are co-prime numbers")
else:
    print(f"{a} and {b} are not co-prime numbers")