class Prime:
    def __init__(self,num):
        self.number = num
        
    def prime_nor_composite(self):
        if self.number == 1:
            print("1 is neither prime nor composite")
    
    def check_prime(self):
        if self.number == 1:
            return x1.prime_nor_composite()
            
        for i in range(2,self.number):
            if self.number % i == 0:
                print (f"{self.number} is composite")
                break;
        else:
            print(f"{self.number} is prime")

num = int(input("Enter a number: "))
x1 = Prime(num)
x1.check_prime()