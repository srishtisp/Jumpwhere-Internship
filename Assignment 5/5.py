# 5. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
# Sample String : 'abc', 'xyz' 
# Expected Result : 'xyc abz'

s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")
s3 = s2[:2] + s1[2:]
s4 = s1[:2] + s2[2:]

s = s3+" "+s4
print(s)
