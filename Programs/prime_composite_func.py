def prime(n):
    if n <= 1:
        return f"{n} is neither prime nor composite."
    for i in range(2, n):
        if n % i == 0:
            return f"{n} is composite number."
    else:
        return f"{n} is a prime number."
num = int(input("Enter a number :"))
print(prime(num))