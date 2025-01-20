def pattern(n):
    if n==1:
        print(1)
    else:
        pattern(n-2)
        print(n)
pattern(7)