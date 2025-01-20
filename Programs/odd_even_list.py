
user_input = input("Enter numbers separated by space: ")
num_list = [int(num) for num in user_input.split()]

odd = []
even = []

for num in num_list:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Odd numbers in the list:", odd)
print("Even numbers in the list:", even)