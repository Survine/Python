a = int(input("Enter the 1st side: "))
b = int(input("Enter the 2nd side: "))
c = int(input("Enter the 3rd side: "))

if a == b == c:
    print("Equilateral Triangle")
elif a == b or b == c or c == a:
    print("Isoceles Triangle")
else:
    print("Scalene Triangle")