# 6) Write a Python class to implement pow(x, n) 

class PowerCalculator:
    def pow(self, x, n):
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n = -n
        
        result = 1
        while n > 0:
            if n % 2 == 1:
                result *= x
            x *= x
            n //= 2
        return result


calc = PowerCalculator()
print(calc.pow(2, 10))   
print(calc.pow(2, -3))     
print(calc.pow(5, 0))      

