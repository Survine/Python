
list = [5, -3, 8, 7, -10, 2, 1, 0, -2, 9]

positive = 0
negative = 0
zero = 0

for num in list:
    if num > 0:
        positive = positive + 1
    elif num < 0:
        negative = negative + 1
    else:
        zero = zero + 1

print(f"Positive numbers: {positive}")
print(f"Negative numbers: {negative}")
print(f"Zero numbers: {zero}")