# 12. Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.

s = input("Enter a string: ")
count=0
for i, v in enumerate(s):
    if i<4 and v.isupper():
        count+=1
if count >= 2:
    print(s.upper())
else:
    print(s)
