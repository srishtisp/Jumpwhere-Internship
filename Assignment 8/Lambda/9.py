# 9) Write a Python program to find the elements of a given list of strings that contain specific substring using lambda. 
# Original list: ['red', 'black', 'white', 'green', 'orange'] 
# Substring to search: ack Elements of the said list that contain specific substring: ['black'] Substring to search: abc Elements of the said list that contain specific substring: [] 


def find_elements_with_substring(lst, substring):
    return list(filter(lambda x: substring in x, lst))

original_list = ['red', 'black', 'white', 'green', 'orange']
substring1 = 'ack'

result1 = find_elements_with_substring(original_list, substring1)
print(f"Elements of the said list that contain substring '{substring1}': {result1}")

substring2 = 'abc'

result2 = find_elements_with_substring(original_list, substring2)
print(f"Elements of the said list that contain substring '{substring2}': {result2}")
