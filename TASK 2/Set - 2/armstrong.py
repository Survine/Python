num = input("Enter a number: ")
t = len(num)
num = int(num)
arm = 0
temp = num

while num > 0:
    digit = num % 10
    arm = arm + digit ** t
    num = num // 10

if temp == arm:
    print(f"{temp} is an Armstrong number")
else:
    print(f"{temp} is not an Armstrong number")