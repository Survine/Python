user_input = input("Enter the numbers separated by space: ")
num_list = [int (num) for num in user_input.split()]
num_list.sort()
print(f"2nd minimum number is: {num_list[1]}")
print(f"2nd maximum number is: {num_list[-2]}")