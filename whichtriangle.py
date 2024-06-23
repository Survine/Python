a = int(input("Enter the first side of the triangle: "))
b = int(input("Enter the second side of the triangle: "))
c = int(input("Enter the third side of the triangle: "))
if a == b == c:
    print("Equilateral Triangle")
elif a == b or b == c or c == a:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")
