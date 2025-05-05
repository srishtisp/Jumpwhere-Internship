# 8) Write a Python program to check whether a given string contains a capital letter, a lower case letter, a number and a minimum length using lambda. Minimum length : 10 input string: PaceWisd0m o/p: valid string 


is_valid_string = lambda s: (any(c.isupper() for c in s) and   
                             any(c.islower() for c in s) and   
                             any(c.isdigit() for c in s) and    
                             len(s) >= 10)                     

input_string = "PaceWisd0m"

if is_valid_string(input_string):
    print("Valid string")
else:
    print("Invalid string")
