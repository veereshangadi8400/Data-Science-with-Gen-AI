# 1. Write a Python program to execute a string containing Python code.
# def execute_string(s):
#     print(s)
# execute_string('mahesh')

# 2. Write a function that inputs a number and prints the multiplication table of that number
# def multiply(n):
#     for i in range(1, 10+1):
#         print(n, ' x ', i, ' = ', n*i)
# multiply(6)

# 3. Write a lambda function to calculate the factorial of any number given as input.
# import math
# fact = lambda n :  math.factorial(n)
# print(fact(7))

# 4. Write a function that converts a decimal number to a binary number and vice versa
# def dec_to_bin(n):
#     return bin(n)[2:]
# def bin_to_dec(n):
#     return int(n, 2)
# print(dec_to_bin(9))
# print(bin_to_dec('10100'))

# 5. Write a program to print twin primes less than 1000. If two consecutive odd numbers are both 
# prime then they are known as twin primes
# def is_prime(n):
#     if n <= 1:
#         return False
#     i = 2
#     while i*i <= n:
#         if n % i == 0:
#             return False
#         i += 1
#         return True
# limit = 1000
# start = 3
# pair_count = 0
# while start < limit:
#     if is_prime(start) and is_prime(start + 2):
#         print(start, start + 2)
#         pair_count += 1
#     start += 2

# 6. Write a program that can filter odd numbers in a list by using the filter function
# def odd(n):
#     if n%2 == 0:
#         return False
#     else:
#         return True
# f = filter(odd, range(1, 100))
# for i in f:
#     print(i, end=' ')
    

# 7. Write a program that can map() to make a list whose elements are cubes of elements in a given 
# list
# print(list((map(lambda x:x**3, range(1, 10)))))

# 8. Write a program to zip 3 iterables of unequal lengths to get the resultant iteration of the size of 
# the longest input iterable. Use ‘#’ in the place of missing values in the other 2 short iter
# ables.
# num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# squares = [1, 4, 9, 16, 25]
# cubes = [1, 8, 27, 64]
# from itertools import zip_longest as zl
# print(list(zl(num, squares, cubes, fillvalue='#')))

# 9. Write a program using reduce to find the sum of numbers of the given list
# from functools import reduce
# from operator import add
# print(reduce(lambda x, y: x+y, range(1, 10)))
# print(reduce(add, range(1, 10)))

# 10. Write a recursive function to calculate x power n, given x and n as inputs
# def pow(x, n):
#     if n == 0 :
#         return 1
#     if n < 0:
#         return 1 / pow(x, -n)
#     if n%2 == 0:
#         half = pow(x, n//2)
#         return half * half
#     if n%2 != 0:
#         return x * pow(x, n-1)
# print(pow(2, 8))

# 11. Write a program that can filter email ids in a list of strings by using the filter function. 
# 12. Write a function that counts vowels and consonants in a word. 
# 13. Write a Python function to check whether a number is "Perfect" or not. In number theory, a 
# perfect number is a positive integer that is equal to the sum of its proper positive divisors, that is, 
# the sum of its positive divisors excluding the number itself (also known as its aliquot sum). 
# 14.  Write a program to reverse any integer given as input. For example, if input is 120 then output is 
# 21, for input -123 output is -321. 
# 15. Write a program to convert the given Roman numeral to an integer 
# 16. You are given an integer represented as a list of digits, where each digit [i] is the ith digit of the integer. 
# The digits are ordered from most significant to least significant in left-to-right order. The integer does 
# not contain any leading 0's. Increment the given integer by one and return the resulting list of 
# digits. 