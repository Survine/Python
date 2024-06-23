string = input("Enter a string: ")
letter = 0
number = 0
for char in string:
    if char.isalpha():
        letter = letter + 1
    elif char.isdigit():
        number = number + 1
print("Number of letters:", letter)
print("Number of digits:", number)