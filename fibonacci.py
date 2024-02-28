# Print Fibonacci series

'''
def fibo(a):
    a = 0
    b = 1
    print(a)
    print(b)

    for i in range(2, n):
        c = a + b
        a = b
        b = c
        print(c)


n = int(input("Enter a number to print fibonacci series :"))
print(fibo(n))
'''

# Fibonacci Series with recursion


def fibo(a):
    if a < 2:
        return a
    else:
        return fibo(a-1) + fibo(a-2)


n = int(input("Enter a number to print fibonacci series :"))
for i in range(0, n):
    print(fibo(i))
