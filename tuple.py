# 1) Program to Find the size of a Tuple
# tuple1 = (1, 2, 3, 4, (5, 6), 7, 8, 9)
# print(len(tuple1))

# 2) Create a list of tuples from given list having number and its cube in each tuple
# list1 = [(1, 1), (2, 8), (3, 27,), (4, 64)]
# for i in list1:
#     print(i)
 
# 3) Adding Tuple to List and vice – versa
# list1 = [(1, 1), (2, 8), (3, 27,), (4, 64)]
# list1.append((3, 4))
# tuple1 = (1, 2, [3, 4], 5)
# tuple1[2].append(17)
# print(tuple1)

# 4) Sum of tuple elements
# tuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# print(sum(tuple1))

# 5) Modulo of tuple elements
# tuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# divisor = 4
# tuple2 = (i % divisor for i in tuple1)
# for i in tuple2:
#     print(i)

# 6) Row-wise element Addition in Tuple Matrix
# matrix = ((1, 2, 3), 
#           (4, 5, 6), 
#           (7, 8, 9))
# row_sum = tuple(sum(row) for row in matrix)
# print(row_sum)

# 7) Multiply Adjacent elements in a tuple and add result to a new tuple.
# tuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# tuple2 = tuple(tuple1[i] * tuple1[i + 1] for i in range(len(tuple1) - 1))  
# print(tuple2)

# 8) Join Tuples if similar initial element
# tuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# tuple2 = (1, 5, 4, 6, 8)
# if tuple1[0] == tuple2[0]:
#     print(tuple1 + tuple2)

# 9) All pair combinations of 2 tuples
# tuple1 = (1, 2, 3)
# tuple2 = (1, 5, 4)
# print(tuple((x, y) for x in tuple1 for y in tuple2))

# 10) Remove Tuples of Length K from a list.
# list1 = [(1, 2), (3, 4, 5), (6,), (7, 8, 9, 10), (11, 12)]
# list2 = [t for t in list1 if len(t) != 2]
# print(list2)

# 11) Remove Tuples from the List having every element as None
# list1 = [(1, 2), (3, 4, 5), (None,), (7, 8, 9, 10), (None, 12)]
# list2 = [i for i in list1 if not all(item is None for item in i)]
# print(list2)

# 12) Sort a list of tuples by second Item
# tuples_list = [(1, 5), (3, 2), (6, 8), (4, 1)]
# tuples_list.sort(key=lambda x:x[1])
# print(tuples_list)

# 13) Python – Sort Tuples by Total digits
# tuples_list = [(12, 456), (7, 8, 9), (1234, 5), (99999,)]
# tuples_list2 = [i for i in tuples_list]

# 14) Python – Elements frequency in Tuple
# tup = (1, 2, 3, 2, 4, 1, 2, 5, 1, 3)
# frequency = {i: tup.count(i) for i in tup}
# print(frequency)

# 15) Python – Test if tuple is distinct
tup = (1, 2, 3, 4, 5)
def is_distict(tup):
    if len(tup) == len(set(tup)):
        return True
    else:
        return False
print(is_distict(tup))
