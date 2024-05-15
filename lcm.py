num1= int(input("Enter first number: "))
num2= int(input("Enter second number: "))
maxnum= max(num1,num2)

while True:
    if maxnum % num1 == 0 and maxnum % num2 == 0:
        break
    maxnum= maxnum+1
print(f"LCM of {num1} and {num2} is {maxnum}")