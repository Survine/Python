a = int(input("Enter the 1st Number: "))
b = int(input("Enter the 2nd Number: "))

while (a>0 and b>0):
    if a>b:
        a = a%b
    else:
        b = b%a

if a==0:
    print(b)
else:
    print(a)