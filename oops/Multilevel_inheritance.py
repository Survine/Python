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
    
class PrimeFactor(Factor):
    def __init__(self,num):
        Factor.__init__(self,num)
        
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