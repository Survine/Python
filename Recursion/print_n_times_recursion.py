def printName(i,n):
    if i>n:
        return
    else:
        print("Hriday")
        printName(i+1,n)
        

n = int(input("Enter the number of times you want to print: "))
printName(1,n)