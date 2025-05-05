# 4) Write a Python program to find if a given string starts with a given character using Lambda.


starts_with = lambda s, char: s.startswith(char)
string = "Hello, world!"
char = "H"

result = starts_with(string, char)
print(result)  

