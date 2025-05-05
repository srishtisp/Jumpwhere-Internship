# 17. Using range(1,101), make three list, 
# one containing all even numbers
# one containing all odd numbers 
# One containing only prime numbers..

e = []
o = []
p = []

for i in range(1, 101):
    if i%2 == 0:
        e.append(i)
    else:
        o.append(i)
    if i>1:
        flag = 0
        for j in range(2, int(i**0.5)+1):
            if i%j == 0:
                flag = 1
                break
        if flag==0:
            p.append(i)

print("Even numbers:", e)
print("Odd numbers:", o)
print("Prime numbers:", p)
