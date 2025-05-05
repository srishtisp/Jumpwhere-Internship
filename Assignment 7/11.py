# 11. Write a Python program to sort a dictionary by key.

my_dict = {'b': 200, 'a': 100, 'c': 300}


sorted_dict = dict(sorted(my_dict.items()))


print("Dictionary sorted by keys:")
print(sorted_dict)