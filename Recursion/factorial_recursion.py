def fact(a):
    if a == 0:
        return 1
    else:
        return a*fact(a-1)


n = int(input("Enter a number : "))
print(fact(n))