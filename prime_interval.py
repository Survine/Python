# Prime number in a interval

lower = int(input("Enter a Range from where prime number starts :"))
upper = int(input("Enter a Range from where prime number ends :"))
for n in range(lower, upper+1):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            print(n)
