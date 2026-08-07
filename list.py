# 1) Python program to interchange first and last elements in a list
# list1 = [3, 2, 4, 7, 9, 6, 5, 8]
# first = list1[0]
# list1[0] = list1[len(list1) - 1]
# list1[len(list1) - 1] = first
# print(list1)

# 2) Python program to swap two elements in a list
# list1 = [3, 2, 4, 7, 9, 6, 5, 8]


# 3) Python program to find ways to get the length of list 
# list1 = [3, 2, 4, 7, 9, 6, 5, 8]
# print(len(list1))
# count = 0
# for i in list1:
#     count += 1
# print(count)

# 4) Python program to check if element exists in list in different ways.
# list1 = [3, 2, 4, 7, 9, 6, 5, 8]
# status = False
# target = 6
# if target in list1:
#     status = True
# print(status, 'element is present in list')
 
# 5) Different ways to clear a list in Python
# list1 = [3, 2, 4, 7, 9, 6, 5, 8]
# print(list1.clear()) # returns None

# 6) Python program to Reversing a List
# list1 = [3, 2, 4, 7, 9, 6, 5, 8]
# for i in range(len(list1)):
#     list1.insert(i, list1.pop())
# print(list1)
 
# 7) Python program to Cloning or Copying a list without using inbuilt function.
# list1 = [3, 2, 4, 7, 9, 6, 5, 8]
# list2 = []
# for i in list1:
#     list2.append(i)
# print(list2)

# 8) Python program to Count occurrences of an element in a list
# list1 = [3, 2, 4, 7, 9, 6, 5, 8, 9, 9]
# print(list1.count(7))

# 9) Python Program to find sum and average of List in Python
# list1 = [3, 2, 4, 7, 9, 6, 5, 8]
# sum = 0
# average = 0
# for i in list1:
#     sum += i
# print(sum, sum/len(list1))

# 10) Python program to Sum of number digits in List
# list1 = [3, 2, 4, 7, 9, 6, 5, 8]
# print(sum(list1))

# 11) Python program to Multiply all numbers in the list
# list1 = [3, 2, 4, 7, 9, 6, 5, 8]
# product = 1
# for i in list1:
#     product *= i
# print(product)

# 12) Python program to find smallest number in a list
# list1 = [3, 2, 4, 7, 9, 6, 5, 8]
# min = list1[0]
# for i in list1:
#     if i < min:
#         min = i
# print(min)

# 13) Python program to find largest number in a list
# list1 = [3, 2, 4, 7, 9, 6, 5, 8]
# print(max(list1))
# print(min(list1))

# 14) Python program to find second largest number in a list
# list1 = [3, 2, 4, 7, 9, 6, 5, 8]
# list1.sort()
# print(list1[-2])

# 15) Python program to print even numbers in a list
# list1 = [3, 2, 4, 7, 9, 6, 5, 8]
# for i in list1:
#     if i % 2 == 0:
#         print(i)

# 16) Python program to print odd numbers in a List
# list1 = [3, 2, 4, 7, 9, 6, 5, 8]
# for i in list1:
#     if i % 2 != 0:
#         print(i)
 
# 17) Python program to print all even numbers in a range
# list1 = [3, 2, 4, 7, 9, 6, 5, 8]
# for i in range(15):
#     if i % 2 == 0:
#         print(i)
 
# 18) Python program to print all odd numbers in a range
# for i in range(15):
#     if i % 2 != 0:
#         print(i)

# 19) Python program to count Even and Odd numbers in a List
# list1 = [3, 2, 4, 7, 9, 6, 5, 8]
# even = 0
# odd = 0
# for i in list1:
#     if i % 2 == 0:
#         even += 1
#     else:
#         odd += 1
# print(even, odd)

# 20) Python program to print positive numbers in a list
# import random
# num = random.choices(range(-10, 10), k=12)
# print(num)
# for i in num:
#     if i > 0:
#         print(i)

# 21) Python program to print negative numbers in a list
# import random
# num = random.choices(range(-10, 10), k=12)
# print(num)
# for i in num:
#     if i < 0:
#         print(i)

# 22) Python program to print all positive numbers in a range
# for i in range(-10, 13):
#     if i > 0:
#         print(i)

# 23) Python program to print all negative numbers in a range
# for i in range(-10, 13):
#     if i < 0:
#         print(i)

# 24) Python program to count positive and negative numbers in a list
# pos = 0
# neg = 0
# for i in range(-10, 13):
#     if i > 0:
#         pos += 1
#     else:
#         neg += 1
# print(pos, neg)

# 25) program to Remove multiple elements from a list in Python
# list1 = [3, 2, 4, 7, 9, 6, 5, 8]
# for i in list1[:]:
#     if i > 5:
#         list1.remove(i)
# print(list1)

# 26) Python program to Remove empty tuples from a list
# tuples_list = [(), ('a', 'b'), (), ('c', 'd', 'e'), (), ('f',)]
# # filtered_list = [t for t in tuples_list if t]
# filtered_list = [t for t in tuples_list if len(t) > 0]
# # filtered_list = list(filter(None, tuples_list))
# print(filtered_list)

# 27) Python program to print duplicates from a list of integers
# list1 = [3, 2, 4, 7, 9, 6, 5, 8, 9, 4, 5, 6, 3, 2, 7, 1]
# list2 = list(set(list1))
# print(list2)