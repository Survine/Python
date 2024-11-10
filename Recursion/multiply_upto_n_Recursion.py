def product_upto_n(n):
    if n == 1:
        return 1
    else:
        return n * product_upto_n(n-1)
num = int(input("Enter a number :"))
print(product_upto_n(num))