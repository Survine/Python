def factor(num, n=1):
    if n <= num:
        if num % n == 0:
            print(n, end=",")
        factor(num, n+1)
    else:
        return

num = int(input("Enter a number: "))
factor(num)