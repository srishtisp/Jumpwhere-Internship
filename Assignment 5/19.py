# 19. Write a Python program to find smallest and largest word in a given string.

s = input('Enter a string: ')
l = s.split()
print('Smallest:', min(l, key=len))
print('Largest:', max(l, key=len))
