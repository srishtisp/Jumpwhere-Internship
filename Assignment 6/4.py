# 4. Write a Python program to check a triangle is equilateral, isosceles or scalene.
# Note :
# An equilateral triangle is a triangle in which all three sides are equal.
# A scalene triangle is a triangle that has three unequal sides.
# An isosceles triangle is a triangle with two equal sides.
# Expected Output:
# Input lengths of the triangle sides:                                    
# x: 6                                                                    
# y: 8                                                                    
# z: 12                                                                   
# Scalene triangle 

s1 = int(input('Enter length of the first side :'))
s2 = int(input('Enter length of the second side :'))
s3 = int(input('Enter length of the third side :'))
if s1==s2==s3:
    print('Equilateral triangle')
elif s1==s2 or s1==s3 or s2==s3:
    print('Isoceles')
else: print('Scalene') 