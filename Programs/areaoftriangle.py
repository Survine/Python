# Area of triangle

'''
height = float(input("Enter Height of the triangle :"))
base = float(input("Enter Base of the triangle :"))
area = (1/2)*height*base
print(f"The area of triangle of height {height} and base {base} is {area}")
'''

# Area of triangle using Heron's formula

a = float(input("Enter side a :"))
b = float(input("Enter side b:"))
c = float(input("Enter side c:"))
s = (a+b+c)/2
area = s*(s-a)*(s-b)*(s-c)**0.5
print("The area of triangle is ", area)
