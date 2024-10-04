# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0: 
        return False
    
    
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def print_primes_in_range(start, end):
    for num in range(start, end + 1):
        if is_prime(num):
            print(num)

print_primes_in_range(10, 30)
