# Kilometers to Miles and (vice versa)

print("Enter 1 to convert Kilometers --> Miles")
print("Enter 2 to convert Miles --> Kilometers")
ask = int(input("Enter your choice :"))
if ask == 1:
    a = float(input("Enter in Kilometers :"))
    print(f"{a} km will be {a/1.60934} mi")
elif ask == 2:
    b = float(input("Enter in Miles :"))
    print(f"{b} mi will be {b*1.60934} km")
