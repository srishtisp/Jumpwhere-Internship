# 19. From a list containing ints, strings and floats, make three lists to store them separately

l = [1, 'hi', 3.14]
i = []
s = []
f = []
for j in l:
    if isinstance(j, int):
        i.append(j)
    elif isinstance(j,float):
        f.append(j)
    elif isinstance(j,str):
        s.append(j)
print('Integers: ',i)
print('Strings: ',s)
print('Floats: ',f)