# 7. Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'

s = input('Enter a string : ')
i1 = s.find('not')
i2 = s.find('poor')
if i2 > i1 and i1 > 0 and i2 > 0:
    s = s.replace(s[i1:(i2+4)], 'good')
    print(s)
else:
    print(s)