# 1) Sort Dictionaries by Key or Value
# data = {'banana': 3, 'apple': 5, 'cherry': 2, 'date': 4}
# sorted_by_key = dict(sorted(data.items()))
# print(sorted_by_key )
# sorted_by_value = dict(sorted(data.items(), key=lambda item:item[1]))
# print(sorted_by_value)

# 2) Handling missing keys in Python dictionaries
# data = {'banana': 3, 'apple': 5, 'cherry': 2, 'date': 4}
# # print(data['grapes'])
# print(data.get('grapes'))
# print(data.get('grapes', 'unknown'))


# 3) Python program to find the sum of all items in a dictionary
# data = {'a': 100, 'b': 200, 'c': 300}
# print(sum(data.values()))
# data = {'a': 100, 'b': 'invalid', 'c': 300, 'd': None, 'e': 50}
# print(sum(x for x in data.values() if isinstance(x, (int, float))))

# 4) Python program to find the size of a Dictionary
# data = {'a': 100, 'b': 200, 'c': 300}
# print(len(data))

# 5) Program to Merge two Dictionaries
# data = {'a': 100, 'b': 200, 'c': 300}
# data2 = {'a': 100, 'b': 'invalid', 'c': 300, 'd': None, 'e': 50}
# data.update(data2)
# print(data)

# 6) Python – Group Similar items to Dictionary Values List
# tuples_list = [('A', 1), ('B', 2), ('A', 3), ('B', 4), ('C', 5)]
# group = {}
# for key, value in tuples_list:
#     group.setdefault(key, []).append(value)
# print(group)

# 7) Different Ways to remove a key from dictionary
# data = {'a': 100, 'b': 'invalid', 'c': 300, 'd': None, 'e': 50}
# # print(data.pop('a'))
# # print(data)
# del data['a']
# print(data)

# 8) program to replace value of a key in a Dictionary
# data = {'a': 100, 'b': 'invalid', 'c': 300, 'd': None, 'e': 50}
# data['b'] = 1000
# print(data)

# 9) program to remove all duplicates values in a given dictionary
# data = {'a': 10, 'b': 20, 'c': 10, 'd': 30, 'e': 20}
# result = {}
# seen = set()
# for k, v in data.items():
#     if v not in seen:
#         result[k] = v
#         seen.add(v)
# print(result)

# 10) Program to create a dictionary with keys are unique elements of string and values as 
# frequency of the char in the string
# text = "programming"
# frequency = {}
# for i in text:
#     frequency[i] = frequency.get(i, 0) + 1
# print(frequency)
# frequency = {i:text.count(i) for i in set(text)}
# print(frequency)
# from collections import Counter
# print(dict(Counter(text)))
    
# 11) program to calculate the mean of Values in a Dictionary.
# data = {'a': 10, 'b': 20, 'c': 10, 'd': 30, 'e': 20}
# count = 0
# print(sum(data.values()) / len(data))

# 12) program to find the Maximum record value's key in a dictionary
# data = {'a': 10, 'b': 20, 'c': 10, 'd': 30, 'e': 20}
# # max_key = max(data, key=data.get)
# # print(max_key)
# max_key = max(data.values())

# 13) way to extract values of Particular Key in Nested dictionaries.
# employees = {
#     "emp1": {"name": "Alice", "role": "Developer", "salary": 90000},
#     "emp2": {"name": "Bob", "role": "Designer", "salary": 80000},
#     "emp3": {"name": "Charlie", "role": "Manager", "salary": 110000},
# }
# print(employees.get('emp3').get('role'))
