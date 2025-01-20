def reorganize_string(str):
    n = len(str)
    
    for i in range(1,n):
        if i == n-1:
            return str
        if str[i-1] == str[i]:
            if str[i] != str[i+1]:
                swap(str[i],str[i+1])
                return str

def swap(a,b):
    return b,a

#main
str = input("Enter a string")
print(reorganize_string(str))