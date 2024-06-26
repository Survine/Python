# Printing Multiplication table 

n = int(input("Enter the table number :"))
for i in range(1, 11):
    m = n*i
    print(f"{n} x {i} = {m}")
