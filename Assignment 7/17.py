# 17. Write a Python program to match key values in two dictionaries.
# Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
# Expected output: key1: 1 is present in both x and y

dict_x = {'key1': 1, 'key2': 3, 'key3': 2}
dict_y = {'key1': 1, 'key2': 2}


for key in dict_x:
    if key in dict_y and dict_x[key] == dict_y[key]:
        print(f"{key}: {dict_x[key]} is present in both dict_x and dict_y")
