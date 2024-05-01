def find_factors(n, i=1, factors=[]):
    if i > n:
        return factors
    if n % i == 0:
        factors.append(i)
    return find_factors(n, i + 1, factors)

# Test the function
number = int(input("Enter a number: "))
result = find_factors(number)
print("Factors of", number, "are:", result)