# 18. Write a Python program to swap comma and dot in a string.
# Sample string: "32.054,23"
# Expected Output: "32,054.23"

s = input('Enter a string : ')
l = s.split('.')
n = []
for i in l:
    n.append(i.replace(',','.'))
s1 = ','.join(n)
print(s1)
