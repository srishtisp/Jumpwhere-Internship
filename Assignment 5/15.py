# 15. Write a Python program to count repeated characters in a string.
# Sample string: 'thequickbrownfoxjumpsoverthelazydog'
# Expected output :
# o 4
# e 3
# u 2
# h 2
# r 2
# t 2

from collections import Counter

s = input('Enter a string : ')
freq = Counter(s)
for i,v in freq.items():
    if v>1:
        print(i, v)