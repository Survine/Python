email = input("Enter an email address: ")

if "@" in email and "." in email:
    print("The email address is valid.")
else:
    print("The email address is invalid.")