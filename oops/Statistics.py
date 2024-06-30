import statistics

class Stats:
    def __init__(self):
        self.data = []

    def add_data(self, nums):
        self.data.extend(nums)

    def mean(self):
        return statistics.mean(self.data)

    def median(self):
        return statistics.median(self.data)

    def mode(self):
        return statistics.mode(self.data)


obj = Stats()

num_list = input("Enter numbers separated by space: ").split()
num_list = [int(num) for num in num_list]
obj.add_data(num_list)


while True:
    print('1. Print Mean')
    print('2. Print Median')
    print('3. Print Mode')
    print('4. Enter Another Number')
    print('5. Show Mean, Median and Mode')
    print('6. Exit')
    
    n = input('Choose an option: ')
    
    if n == '1':
        print('Mean is:', obj.mean())
    
    elif n == '2':
        print('Median is:', obj.median())
    
    elif n == '3':
        print('Mode is:', obj.mode())
    
    elif n == '4':
        new_nums = input('Enter numbers separated by space: ').split()
        new_nums = [int(num) for num in new_nums]
        obj.add_data(new_nums)
        print('Numbers added.')
    
    elif n == '5':
        print('Mean is:', obj.mean())
        print('Median is:', obj.median())
        print('Mode is:', obj.mode())
    
    elif n == '6':
        break
    
    else:
        print('Invalid Input!')
