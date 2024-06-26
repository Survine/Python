class HCF_LCM:
    def __init__(self, num1, num2):
        self.number1 = num1
        self.number2 = num2

    def find_HCF(self):
        smallest = min(self.number1, self.number2)
        for i in range(1,smallest + 1):
            if (self.number1 % i == 0) and (self.number2 % i == 0):
                hcf = i
        return hcf

    def find_LCM(self):
        largest = max(self.number1, self.number2)
        while True:
            if largest % self.number1 == 0 and largest % self.number2 == 0:
                lcm = largest
                break
            largest += 1
        return lcm
n1 = int(input("Enter 1st number: "))
n2 = int(input("Enter 2nd number: "))
x1 = HCF_LCM(n1, n2)
print("HCF:", x1.find_HCF())
print("LCM:", x1.find_LCM())