# 5. Write a Python program to iterate over dictionaries using for loops.

my_dict = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York'
}


print("\nKey-Value Pairs:")
for key, value in my_dict.items():
    print(f"{key}: {value}")
