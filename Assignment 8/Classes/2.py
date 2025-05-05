# 2) Write a Python class to find validity of a string of parentheses, '(', ')', '{', '}', '[' and ']. These brackets must be close in the correct order, for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid. 

class ParenthesesValidator:
    def __init__(self):
        self.pair_map = {')': '(', '}': '{', ']': '['}

    def is_valid(self, s):
        stack = []
        for char in s:
            if char in self.pair_map.values():  
                stack.append(char)
            elif char in self.pair_map: 
                if not stack or stack[-1] != self.pair_map[char]:
                    return False
                stack.pop()
            else:
                return False  
        return len(stack) == 0

validator = ParenthesesValidator()

print(validator.is_valid("()"))       
print(validator.is_valid("()[]{}"))   
print(validator.is_valid("[]"))        
print(validator.is_valid("({[)]"))     
print(validator.is_valid("{{{"))       
