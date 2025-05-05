# 11. A school has following rules for grading system:
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A
# Ask user to enter marks and print the corresponding grade.

m = int(input('Enter marks: '))
if m>100 or m<0:
    print('Invalid marks')
else:
    print('Grade: ')
    if m>80:
        print('A')
    elif 60<m<80:
        print('B')
    elif 50<m<60:
        print('C')
    elif 45<m<50:
        print('D')
    elif 25<m<45:
        print('E')
    else: print('F')