import copy

# Original list
org = [1, 2, [3, 4], 5]

# Shallow copy
shallow = copy.copy(org)

# Deep copy
deep = copy.deepcopy(org)

# Modifying the original list
org[2][0] = 'Changed'

print("Original List:", org)
print("Shallow Copied List:", shallow)
print("Deep Copied List:", deep)