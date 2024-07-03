class Num1:
    def __init__(self, a):
        self.number1 = a

class Num2:
    def __init__(self, b):
        self.number2 = b

class HCF_LCM(Num1, Num2):
    def __init__(self, a, b):
        Num1.__init__(self, a)
        Num2.__init__(self, b)
    
    def find_HCF(self):
        smallest = min(self.number1, self.number2)
        hcf = 1  
        for i in range(1, smallest + 1):
            if (self.number1 % i == 0) and (self.number2 % i == 0):
                hcf = i
        return hcf

    def find_LCM(self):
        largest = max(self.number1, self.number2)
        lcm = largest
        while True:
            if lcm % self.number1 == 0 and lcm % self.number2 == 0:
                break
            lcm += 1
        return lcm

obj = HCF_LCM(12, 15)
print("HCF is: ", obj.find_HCF())  
print("LCM is: ", obj.find_LCM())  