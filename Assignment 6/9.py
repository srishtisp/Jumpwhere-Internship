# 9. A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
# Ask user for quantity
# Suppose, one unit will cost 100.
# Judge and print total cost for user.

q = int(input('Enter quantity of products :'))
total = q*100
if total>1000:
    disc = total*0.1
    cost = total-disc
    print('Discount =', disc)
    print('Cost =', cost)
else: print('No discount. Cost = ', total)

