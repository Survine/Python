def ntimesfromback(i,n):
    if i > n:
        return
    else:
        ntimesfromback(i+1,n)
        print(i)

n = int(input("Enter the number: "))
ntimesfromback(1,n)