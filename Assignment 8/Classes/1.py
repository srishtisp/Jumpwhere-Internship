# 1) Write a python class to convert an integer into a roman numeral and viceversa

class RomanConverter:
    def __init__(self):
        self.int_to_roman_map = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        self.roman_to_int_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

    def int_to_roman(self, num):
        roman = ''
        for value, symbol in self.int_to_roman_map:
            while num >= value:
                roman += symbol
                num -= value
        return roman

    def roman_to_int(self, roman):
        total = 0
        prev_value = 0
        for char in reversed(roman):
            value = self.roman_to_int_map[char]
            if value < prev_value:
                total -= value
            else:
                total += value
                prev_value = value
        return total


converter = RomanConverter()


print(converter.int_to_roman(188))  

print(converter.roman_to_int("CLXXXVIII"))