char = input("Enter a Character: ")
if char.isupper():
    print(f"The given character {char} is in Upper case")
elif char.islower():
    print(f"The given character {char} is in Lower case")
else:
    print(f"The given character {char} is not an alphabet")