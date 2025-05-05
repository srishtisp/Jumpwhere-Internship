# 20. Write a Python program to remove all consecutive duplicates of a given string.

s = input('Enter a string : ')
l = ' '
for i in s:
    if i==l[-1]:
        continue
    else:
        l+=i
print(l)