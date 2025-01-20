my_list = [int(x) for x in input("Enter a list of numbers separated by space: ").split()]
sq = lambda x: x*x
sq_list = [sq(x) for x in my_list]
print(sq_list)