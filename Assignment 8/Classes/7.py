# 7) Write a Python class to reverse a string word by word. 
# Input string : 'hello .py' Expected Output : '.py hello' 

class StringReverser:
    def reverse_words(self, s):
        words = s.strip().split()
        return ' '.join(reversed(words))
    
reverser = StringReverser()
input_string = 'what *is'
print(reverser.reverse_words(input_string)) 