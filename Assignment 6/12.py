# 12. A student will not be allowed to sit in exam if his/her attendence is less than 75%.
# Take following input from user
# Number of classes held
# Number of classes attended.
# And print
# percentage of class attended
# Is student is allowed to sit in exam or not.

held = int(input('Enter no. of classes held: '))
attended = int(input('Enter no. of classes attended: '))
p = (attended/held)*100
print('Percentage attended: ',p)
if p>74: 
    print('Allowed to sit in exam.')
else: print('Not allowed to sit in exam.')
