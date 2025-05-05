# 13. Take 10 integers from keyboard using loop and print their average value on the screen.

n = []
print('Enter 10 numbers: ')
for i in range(10):
    n.append(int(input()))
avg = sum(n)/len(n)
print('Average: ',avg)