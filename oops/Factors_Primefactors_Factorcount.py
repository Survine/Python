class Factor:
    def __init__(self,num):
        self.num = num
        
    def calc_factors(self):
        factor_list =[]
        for i in range(1,self.num + 1):
            if self.num % i == 0:
                factor_list.append(i)
        return factor_list
        
    def prime_factor(self):
        prime_list = []
        for i in self.calc_factors():
            if i > 1:
                for j in range(2,i):
                    if i % j == 0:
                        break
                else:
                    prime_list.append(i)
        return prime_list
                
              
    def factor_count(self):
        return len(self.calc_factors())
        
        
num = int(input("Enter a number: "))
x1 = Factor(num)
print("Factor :",x1.calc_factors())
print("Prime Factor :",x1.prime_factor())
print("Factor Count:",x1.factor_count())