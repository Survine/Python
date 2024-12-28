def positive(x):
    return x >= 0

numbers = [12, -7, 5, 64, -14]
positive_numbers = list(filter(positive, numbers))
print(positive_numbers)