# 10. A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
# Ask user for their salary and year of service and print the net bonus amount.

y = int(input('Enter years of service: '))
if y>5:
    sal = int(input('Bonus applicable ! Enter salary: '))
    tsal = sal+(sal*0.05)
    print('Net bonus with salary = ', tsal)
else: print('No bonus')