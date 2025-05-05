# 16. Take inputs from user to make a list. Again take one input from user and search it in the list and delete that element, if found. Iterate over list using for loop.

l = []
flag = 0
n = int(input('Length of the list: '))
print('Enter',n,'elements: ')
for i in range(n):
    temp = int(input())
    l.append(temp)
key = int(input('Enter element to search: '))
for i in l:
    if i==key:
        flag+=1
        l.remove(key)
        print('Element found and deleted. Remaining elements: ')
        print(l)
if flag==0:
    print('Element not found.')