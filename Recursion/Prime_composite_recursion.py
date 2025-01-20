def isprime(n, i=2):
    if n <= 1:
        return f"{n} is neither prime nor composite."
    elif n == 2:
        return f"{n} is a prime number."
    elif n % i == 0:
        return f"{n} is a composite number."
    elif n%2!=0:
        return f"{n} is a prime number."
    else:
        return isprime(n, i + 1)

print(isprime(18))