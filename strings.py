# 1) name = ‘Mahesh babu’. Reverse words in a given String. 

name = 'mahesh babu!'
# words = name.split()
# words.insert(0, words.pop())
# print(words)

# 2) How to get the 3th character in name variable. 
# print(name[2])

# 3) How to remove 3th character in name variable. 
# name = 'Mahesh babu'
# new_name = name[:2] + name[3:]
# print(new_name)

# 4) How to get the 7th character till end of the content in name variable. 
# name = 'Mahesh babu'
# print(name[7:])

# 5) How to remove 7th character till end of the content in name variable. 
# name = 'Mahesh babu'
# new_name = name[:7]
# print(new_name)

# 6) Find the length of name variable. 
# name = 'Mahesh babu'
# print(len(name))

# 7) remove Spaces in name variable. 
# name = 'Mahesh babu'
# print(name[:6] + name[7:])

# 8) Change the characters in name variable to all uppercase. 
# print(name.upper())

# 9) slicing in Python to rotate name 

        

# 10) Verify all methods in String class. 
# print(dir(str))

# 11) Check if a ‘babu’ is present in name or  not. 
# print('babu' in name)

# 12) Remove ‘babu’from name 
# print(name.replace('babu', ''))

# 13) Find the content of name till ‘babu’ 
# print(name[:7])

# 14) Python program to check whether the string is Symmetrical or Palindrome
# print(name == name[::-1])
# print(name[::-1])

# 15) Reverse words in a given String in Python
# words = name.split()
# words.insert(0, words.pop())
# print(words[0], words[1])

# 16) Ways to remove i’th character from string in Python
# print(name.replace(name[5], ''))
# print(name.replace(' ', ''))
 
# 17) Find length of a string in python (4 ways)
# print(len(name))
# length = 0
# for _ in name:
#     length += 1
# print(length)
 
# 18) Python – Avoid Spaces in a given string 
# print(name.replace(' ', ''))

# 19) Python program to print even length words in a string
# count = 1
# for _ in name: 
#     if count <= len(name) - 1:
#         print(name[count])
#         count += 2

# 20) Python – Uppercase Half String
# halfName = name[:int((len(name) -1) / 2)]
# print(halfName.upper())

# 21) Python program to capitalize the first and last character of each word in a string 
# words = name.split()
# result = []
# for word in words:
#     if len(word) == 1:
#         result.append(word.upper())
#     else:
#         transformed = word[0].upper() + word[1:-1] + word[-1].upper()
#         result.append(transformed)
# print(result)

# 22) Python program to check if a string has at least one letter and one number
# has_letter = False
# has_number = False
# status = False
# for char in name:
#     if char.isalpha():
#         has_letter = True
#     if char.isnumeric():
#         has_number = True
# if has_number and has_letter:
#     status = True
# print(status)

# 23) Python Program to accept the strings which contains all vowels
# word = input('Enter any string: ')
# vowels = set('aeiou')
# str_char = set(word.lower())
# if vowels.issubset(str_char):
#     print(word, 'contain all vowels')
# else:
#     print(word, 'does not contain all vowels')

# 24) Python program Count the Number of matching characters in a pair of string
# word1 = 'Veeresh'
# word2 = 'Mahesh'
# count = set()
# for char in word1.lower():
#     if char in word2.lower():
#         count.update(char)
# print(count)
# print(len(count))
    

# 25) Python program to count number of vowels using sets in given string
# vowels = set()
# for char in name.lower():
#     if char in 'aeiou':
#         vowels.update(char)
# print(vowels, len(vowels))

# 26) Python Program to remove all duplicates from a given string 
# noDuplicate = ''
# for char in name.lower():
#     if char not in noDuplicate:
#         noDuplicate += char
# print(noDuplicate)

# 27) Python program to identify Least Frequent Character in String
# leastFrequency = ''
# for char in name.lower():
#     if char not in leastFrequency:
#         leastFrequency += char
# print(leastFrequency)

# 28) Python program to identify Maximum frequency character in String 
# count = {}
# for char in name.lower():
#     if char not in count:
#         count[char] = 0
#     count[char] += 1
# # maxCount = 0
# # for char in count:
# #     if count[char] > maxCount:
# #         maxCount = count[char]
# print(max(count, key=count.get))
    

# 29) Python program to identify Odd Frequency Characters
# count = {}
# for char in name.lower():
#     if char not in count:
#         count[char] = 0
#     count[char] += 1
# for key, value in count.items():
#     if (value % 2) != 0:
#         print(key, value)
        
# 30) Python program to identify Specific Characters Frequency in String List 
# count = {}
# for char in name.lower():
#     if char not in count:
#         count[char] = 0
#     count[char] += 1
# if 'h' in count:
#     print('h :', count['h'])

# 31) Python program to identify Frequency of every character in a given String
# frequency = {}
# for char in name.lower():
#     if char not in frequency:
#         frequency[char] = 0
#     frequency[char] += 1
# print(frequency) 

# 32) Python Program to check if a string contains any special character
# status = False
# for char in name:
#     if not char.isalnum() and not char.isspace():
#         print(char)
#         status = True
# print(status)

# 33) Generating random strings until a given string is generated


# 34) Find words which are greater than given length k
# name2 = 'Mahesh Babu is a hero'
# words = name2.split()
# length = 3
# for word in words:
#     if len(word) > length:
#         print(word)

# 35) Python program for removing ith character from a string
# name2 = name.replace(name[4], '')
# print(name2)

# 36) Python program to split and join a string
words = name.split(' ')
print(words)
name2 = ' '.join([words[0], words[1]])
print(name2)

# 37) Python program to find uncommon words from two Strings 
# 38) Python program to Swap commas and dots in a String 
# 39) Python program to get Permutation of a given string without using inbuilt function.