# 8. Write a Python function that takes a list of words and returns the length of the longest one. 

s = input("Enter words separated by a space: ")
s1 = s.split()
s1.sort(key=len)
print(len(s1[-1]))