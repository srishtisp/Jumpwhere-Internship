# 5. Write a Python program to calculate the sum and average of n integer numbers (input from the user). Input 0 to finish

n = []
print('Enter numbers (enter 0 to stop) :')
while True:
    temp = int(input())
    if temp == 0:
        break
    n.append(temp)
s = sum(n)
a = s/len(n) if n else 0
print('Sum : ', s)
print('Average : ', a)