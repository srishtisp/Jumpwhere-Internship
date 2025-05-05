# 16. Write a Python program to print the index of the character in a string.

s = input('Enter a string : ')
c = input('Enter a character : ')
for i,v in enumerate(s):
    if c==v:
        print(i)