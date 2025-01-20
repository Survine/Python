str = input("Enter a string: ")
count = 0
for i in str:
    if i == ' ':
        count += 1
print(f"Number of spaces in {str} is {count}")