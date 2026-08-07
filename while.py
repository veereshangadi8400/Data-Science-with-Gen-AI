# While loop 
# 1) Write a program in Python to display the Factorial of a number.
# n = 6
# i, fact = 1, 1
# if n == 0 or n == 1:
#     fact
# else:
#     while i <= n:
#         fact *= i
#         i += 1
# print(fact)

# 2) Write a program in Python to reverse a word.
# word = 'program' 
# print(word[::-1])

# 3) Write a Python program to reverse a number.
# num = 12345
# # reversedNum = 0
# # while num > 0:
# #     reversedNum = reversedNum * 10 + (num % 10)
# #     num = num // 10
# # print(reversedNum)
# print(int(str(num)[::-1]))

# 4) Write a program to display the first 7 multiples of 7.
# multiples = 0
# i = 1
# while i <= 7:
#     multiples = 7 * i
#     print(multiples)
#     i += 1

# 5) Write a program that appends the square of each number to a new list.
# squares = []
# i = 1
# while i <= 6:
#     squares.append(i**2)
#     i += 1
# print(squares)

# 6) WAP to separate positive and negative number from a list.
# import random
# list1 = random.choices(range(-5, 5), k=7)
# print(list1)
# i = 0
# postive = []
# negative = []
# while i <= len(list1) - 1:
#     if list1[i] >= 0:
#         postive.append(list1[i])
#     else:
#         negative.append(list1[i])
#     i += 1
# print(postive)
# print(negative)

# 7) Write a program that appends the type of elements from a list.
# data = [42, 3.14, "hello", True, [1, 2], {"a": 1}]
# type_list = []
# for _ in data:
#     type_list.append(type(_).__name__)
# print(type_list)

# 8) Write a program to filter even and odd number from a list.
# list1 = [1,2,3,4,5,6,7,8,9]
# even_list = []
# odd_list = []
# for _ in list1:
#     if _ % 2 == 0:
#         even_list.append(_)
#     else:
#         odd_list.append(_)
# print(even_list)
# print(odd_list)

# 9) Write a program to fetch only even values from a dictionary.
# data = {'a': 10, 'b': 15, 'c': 22, 'd': 7, 'e': 40}
# for _ in data:
#     if data[_] % 2 == 0:
#         print(data[_])

# 10) write a program to check the given string is a palindrome or not.
# name = 'pop'
# if name[::-1] == name:
#     print('palindrome')
# else:
#     print('not a palindrome')

# 11) Write a program to check the given number is a prime or not.
# num = 9
# i = 2
# status = True
# while i <= num/2:
#     if num % i == 0:
#        status = False
#        break
#     i += 1
# print(status)

# 12) write a program to print all prime numbers between 0 and user entered number.
# limit = 28
# num = 2
# while num <= limit:
#     i = 2
#     is_prime = True
#     while i * i <= num:
#         if num % i == 0:
#             is_prime = False
#             break
#         i += 1
#     if is_prime:
#         print(num, end=' ')
#     num += 1
    

# 13) Write a program to calculate the sum of all prime numbers between 0 and user entered 
# number.
# limit = 28
# num = 2
# sum = 0
# while num <= limit:
#     i = 2
#     is_prime = True
#     while i*i <= num:
#         if num % i == 0:
#             is_prime = False
#             break
#         i += 1
#     if is_prime:
#         print(num, end=' ')
#         sum += num
#     num += 1
# print('\n',sum)

# 14) write a program to calculate the product of all prime numbers between 0 and user entered 
# number.
# limit = 28
# num = 2
# prod = 1
# while num <= limit:
#     i = 2
#     is_prime = True
#     while i*i <= num:
#         if num%i == 0:
#             is_prime = False
#         i += 1
#     if is_prime:
#         print(num, end=' ')
#         prod *= num
#     num += 1
# print('\n', prod)

# 15) Reverse the entered number by printing the remainder.
# num = 12345
# reve = 0
# while num > 0:
#     remian = num % 10
#     print(remian)
#     reve  = reve * 10 + remian
#     num //= 10
# print(reve)
    

# 16) Reverse the entered number. (Do not print the remainder)
# num = 12345
# print(str(num)[::-1])

# 17) Sum of each digit from a number.
# num = 12345
# sum = 0
# while num > 0:
#     rem = num % 10
#     sum += rem
#     num //= 10
# print(sum)

# 18) Check no. is Armstrong or not.
# num = 1535
# temp = num
# sum = 0
# while temp > 0:
#     rem = temp % 10
#     sum += rem*rem*rem
#     temp //= 10
# if (num == sum):
#     print('ARMSTRONG')
# else:
#     print('not armsron')


# 19) A series program: 1 4 9 16 25 36 and so on
# limit = 8
# start = 1
# while start <= limit:
#     print(start**2)
#     start += 1


# 20) Power of n starting with 1 3.


# 21) Find the factorial of n.
# n = 0
# fact = 1
# if n == 0 or n ==1:
#     fact
# else:
#     i = 1
#     while i <= n:
#         fact *= i
#         i += 1
# print(fact)

# 22) Find average of list of numbers entered through keyboard.
n, i, sum = 8, 1, 0
while i <= n:
    sum += i
    i += 1
print(sum/n)

# 23) Take a number as input and check whether number is 
# 24) calculate the value SUM = 1 + 4 – 9 + 16 – 25 + 36 – … for a given number. 
# 25) calculate the value SUM = 12+22+32+42+52+62+72+.. for a given number. 
# 26) calculate the value SUM = x – x3/3! + x5/5! – x7/7! + x9/9! - for a given number. 
# 27) calculate the value SUM = e1 +e2 +e3 +e4 +e5+… for a given number. 
# 28) calculate the value SUM = 1 + 2 + 6 + 24 + 120 + … for a given number. 
# 29) calculate the value SUM = 1 + 1/4 + 1/9 + 1/16 + 1/25 + for a given number. 
# 30) calculate the value SUM = 1 + 8 + 27 + 64 + … for a given number. 
# 31) To print multiplication table from 1×1 to 10×10. 
# 32) To compute the sum of the digits of a given positive integer number. 
# 33) To read any five real numbers and print the average value. 
# 34) To calculate the sum of first  N natural numbers. 
# 35) To calculate the average of first N odd numbers. 