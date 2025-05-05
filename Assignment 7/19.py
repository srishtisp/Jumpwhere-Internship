# 19. Write a Python program to remove duplicates from a list of lists.
# Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
# New List : [[10, 20], [30, 56, 25], [33], [40]]

sample_list = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]

unique_lists = []
for sublist in sample_list:
    if sublist not in unique_lists:
        unique_lists.append(sublist)

print("New List:", unique_lists)
