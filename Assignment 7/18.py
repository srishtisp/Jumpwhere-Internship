# 18. Write a Python program to check if all dictionaries in a list are empty or not.
# Sample list : [{},{},{}]
# Return value : True
# Sample list : [{1,2},{},{}]
# Return value : False


list1 = [{}, {}, {}]
all_empty = all(not d for d in list1)
print("Are all dictionaries empty?", all_empty)
list2 = [{1, 2}, {}, {}]

all_empty_2 = all(not d for d in list2)

print("Are all dictionaries empty?", all_empty_2)
