def sum(i,n):
    if i < 1:
        print(n)
        return
    else:
        sum(i-1,n+i)
        
sum(5,0)