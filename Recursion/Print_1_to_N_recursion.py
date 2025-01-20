def ntimes(i,n):
    if i > n:
        return
    else:
        print(i)
        ntimes(i+1,n)

n = int(input("Enter a number: "))
ntimes(1,n)