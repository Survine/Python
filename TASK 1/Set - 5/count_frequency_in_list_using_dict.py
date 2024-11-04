my_list = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1]
frequency = {}
for i in my_list:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1
print(frequency)
