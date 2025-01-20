str = input("Enter a string: ")
freq = {i: str.count(i) for i in str}
print(freq)