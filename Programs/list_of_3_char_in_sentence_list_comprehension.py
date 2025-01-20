str = "The quick brown fox jumps over the lazy dog"
my_list = [word for word in str.split() if len(word)>3]
print(my_list)