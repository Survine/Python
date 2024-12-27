<<<<<<< HEAD
=======
def is_palindrome(i, s):
    if i >= len(s) // 2:
        return True
    if s[i] != s[len(s) - i - 1]:
        return False
    return is_palindrome(i + 1, s)


s = "madam"
print(is_palindrome(0, s))  
>>>>>>> 00af1a990760caba0b29322b2e39ef4cec006709
