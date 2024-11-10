def LCM(a,b,n=1):
    if n%a==0 and n%b==0:
        return n
    else:
        return LCM(a,b,n+1)
num1= int(input("Enter first number: "))
num2= int(input("Enter second number: "))
print(f"LCM of {num1} and {num2} is {LCM(num1,num2)}")