# def revntimes(n):
#     if n < 1:
#         return
#     else:
#         print(n)
#         revntimes(n-1)
        
# n = int(input("Enter a number: "))
# revntimes(n)




# Another Way

def revntimes(i,n):
    if i < 1:
        return
    else:
        print(i)
        revntimes(i-1,n)

n = int(input("Enter a number: "))
revntimes(n,n)
