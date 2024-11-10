my_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
sorted_list = sorted(my_list)
if my_list == sorted_list:
    print("List is sorted in ascending order")
elif my_list == sorted_list[::-1]:
    print("List is sorted in descending order")
else:
    print("List is not sorted")