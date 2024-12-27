a = 0
b = 1
count = 0
while count < 10:
    print(a, end=' ')
    c = a + b
    a = b
    b = c
    count += 1