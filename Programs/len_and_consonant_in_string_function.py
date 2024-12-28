def lengthandconsonants(s):
    vowels = 'aeiou'
    consonants = 0
    for i in s:
        if i not in vowels:
            consonants += 1
    print(f"Length of the string is {len(s)} and number of consonants are {consonants}")

str = input("Enter a string: ")
lengthandconsonants(str)