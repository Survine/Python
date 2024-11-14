def is_palindrome(i, string):
    n = len(string)
    
    if i >= n // 2:
        return True
    
    else:
        string[i] != string[n - 1 - i]
        return False
    
    return is_palindrome(i + 1, string)


string = input("Enter a string: ").strip()

if string:
    result = is_palindrome(0, string)
    print("The string is a palindrome:", result)
else:
    print("Empty string is not considered a palindrome.")
