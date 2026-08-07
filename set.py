# 1) Find the size of a Set in Python
# set1 = {1, 2, 3, 4, 5, 6, 7, 8}
# print(len(set1))

# 2) Iterate over a set in Python
# set1 = {1, 2, 3, 4, 5, 6, 7, 8}
# for i in set1:
#     print(i)

# 3) program to identify the maximum and Minimum numbers in numbers Set
# set1 = {1, 2, 3, 4, 5, 6, 7, 8}
# print(max(set1), min(set1))
 
# 4) Remove items from Set
# set1 = {1, 2, 3, 4, 5, 6, 7, 8}
# # set1.remove(8)
# # set1.pop()
# # set1.clear()
# set1.add(1)
# print(set1)

# 5) Check if two lists have at-least one element common using sets.
# set1 = {1, 2, 3, 4, 5, 6, 7, 8}
# set2 = {9, 10, 11, 12, 13, 14, 15, 6}
# print(set1.intersection(set2))

# 6) Find common elements in three lists using sets
# set1 = {1, 2, 3, 4, 5, 6, 7, 8}
# set2 = {9, 10, 11, 12, 13, 14, 15, 7, 6}
# set3 = {16, 17, 18, 19, 20, 21, 22, 23, 24, 7, 6}
# print(set1.intersection(set2.intersection(set3)))

# 7) Find missing and additional values in two lists using sets.
# list1 = [1, 2, 3, 4, 5, 6]
# list2 = [3, 4, 5, 6, 7, 8]
# set1 = set(list1)
# set2 = set(list2)
# missing = list(set1 - set2)
# additional = list(set2 - set1)
# print(missing, additional)
 
# 8) Program to find the difference between two lists using sets.
# list1 = [1, 2, 3, 4, 5, 6]
# list2 = [3, 4, 5, 6, 7, 8]
# print(set(list1).difference(set(list2)))