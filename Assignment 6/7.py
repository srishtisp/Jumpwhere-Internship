# 7. Write a Python program that counts the number of elements within a list that are greater than 30.

l=[]
count = 0
n = int(input('Length of the list: '))
for i in range(n):
    temp = int(input())
    if temp>30:
        count+=1
    l.append(temp)
print(count)