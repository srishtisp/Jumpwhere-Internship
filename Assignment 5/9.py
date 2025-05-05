# 9. Write a Python program to remove the nth index character from a nonempty string.

s = input("Enter a string: ")
n = int(input('Enter an index: '))
s1 = s[:n]+s[n+1:]
print(s1)