str = input("Enter a string: ").lower()
alphabets = "abcdefghijklmnopqrstuvwxyz"
for i in alphabets:
    if i not in str:
        print("Not a Pangram")
        break
else:
    print("Pangram")