str = input("Enter a string: ")
vowels = 'aeiouAEIOU'
for char in str:
    if char in vowels:
        print(char, end=' ')