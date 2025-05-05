# 15. Take integer inputs from user until he/she presses q ( Ask to press q to quit after every integer input ). Print average and product of all numbers.

n = []
print('Enter numbers :')
while True:
    print('Enter q to stop :')
    temp = input()
    if temp == 'q':
        break
    n.append(int(temp))
s = sum(n)
a = s/len(n) if n else 0
print('Sum : ', s)
print('Average : ', a)