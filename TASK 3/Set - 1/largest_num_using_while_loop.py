my_list = [5,8,2,6,1,9,3,7,4]
max=my_list[0]
for i in range(len(my_list)):
    if my_list[i] > max:
        max = my_list[i]
print(max)