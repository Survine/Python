# Merging two dictionaries without using a function

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

# Using dictionary unpacking
merged_dict = {**dict1, **dict2}

print(merged_dict)