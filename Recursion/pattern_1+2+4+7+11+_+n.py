def f(n,x=1):
    if x<=n:
        if x==1:
            print(x,end='')
        else:
            print('+',x,end='',sep='')
        return x + f(n,x+1)
    else:
        return 0
n = 6
s = f(n)
