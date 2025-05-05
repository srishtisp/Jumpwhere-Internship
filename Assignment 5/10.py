# 10. Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically). 
# Sample Words : red, white, black, red, green, black
# Expected Result : black, green, red, white

s = input("Enter words separated by a comma: ")
s1 = [word.strip() for word in s.split(',')]
print(sorted(list(set(s1))))