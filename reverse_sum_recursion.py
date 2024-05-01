def sum_reverse(n):
    if n == 1:
        return 1
    else:
        return n + sum_reverse(n-1)
num = int(input("Enter a number :"))
print(sum_reverse(num))