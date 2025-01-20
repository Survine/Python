s1 = input('Enter the first string: ')
s2 = input('Enter the second string: ')

if sorted(s1) == sorted(s2):
    print('Anagram')
else:
    print('Not an Anagram')