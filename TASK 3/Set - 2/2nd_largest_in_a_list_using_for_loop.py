my_list = [7, 5, 3, 2, 1, 8, 9, 6, 4]
mini = min(my_list)
index = my_list[0]
for i in my_list:
    if mini < i < index:
        index = i
print("Second largest number in the list is:", index)