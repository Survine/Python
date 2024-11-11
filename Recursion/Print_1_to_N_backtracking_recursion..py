def ntimesfromback(i,n):
    if i < 1:
        return
    else:
        ntimesfromback(i-1,n)
        print(i)

n = int(input("Enter the number: "))
ntimesfromback(n,n)