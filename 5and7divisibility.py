
numbers = []
for num in range(100, 27001):
    if num % 7 == 0 and num % 5 == 0:
        numbers.append(num)

for num in numbers:
    print(num)