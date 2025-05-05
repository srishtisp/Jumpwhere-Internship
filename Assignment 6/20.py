# 20.You are given with a list of integer elements. Make a new list which will store square of elements of previous list.

l = list(map(int, input('Enter numbers: ').split()))
nl = []
for i in l:
    nl.append(i*i)
print(nl)