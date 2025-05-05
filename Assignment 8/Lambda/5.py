# 5) Write a Python program to check whether a given string is number or not using Lambda. 


is_number = lambda s: s.replace('.', '', 1).isdigit() if s.count('.') < 2 else False
string = "123.45"
result = is_number(string)

print(result)  

string = "123a"
result = is_number(string)
print(result)  
