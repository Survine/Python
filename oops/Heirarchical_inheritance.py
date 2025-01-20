class Num:
    def __init__(self,num):
        self.num = num
        
class Factor(Num):
    def __init__(self,num):
        Num.__init__(self,num)
        
    def calc_factors(self):
        factor_list =[]
        for i in range(1,self.num + 1):
            if self.num % i == 0:
                factor_list.append(i)
        return factor_list

class Factorial(Num):
    def __init__(self,num):
        Num.__init__(self,num)
        
    def calc_factorial(self):
        fact = 1
        for i in range(1,self.num + 1):
            fact *= i
        return fact

num = int(input("Enter a number: "))
x1 = Factor(num)
x2 = Factorial(num)
print("Factors :",x1.calc_factors())
print("Factorial :",x2.calc_factorial())