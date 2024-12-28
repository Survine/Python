def is_perfect_square(x):
    s = int(x**0.5)
    if x == s * s:
        return True
    else:
        return False


def is_fibonacci_num(n):
    if n < 0:
        return False
    else:
        return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)


num = int(input("Enter a number: "))
if is_fibonacci_num(num):
    print(f"{num} is a Fibonacci number")
else:
    print(f"{num} is not a Fibonacci number")
