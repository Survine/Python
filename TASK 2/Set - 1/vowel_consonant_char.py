char = input("Enter a character: ").lower()

if char in 'aeiou':
    print(f"The character {char} is a vowel.")
elif char.isalpha():
    print(f"The character {char} is a consonant.")
else:
    print("Invalid input, please enter a letter.")
