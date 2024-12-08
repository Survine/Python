n=int(input())
a = [int(i) for i in input().split(' ')]
b=[]
b=a[::-1]
c=[]
for i in range(n):
    c.append(a[i]+b[i])
print(*c,sep=' ',end="")