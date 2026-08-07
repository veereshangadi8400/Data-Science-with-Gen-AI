# 1) Find all of the numbers from 1–1000 that are divisible by 8
# print([i for i in range(1, 1000+1) if i%8 == 0])

# 2) Find all of the numbers from 1–1000 that have a 6 in them
# print([i for i in range(1, 1000) if '6' in str(i)])

# 3) Count the number of spaces in a string (use string "Practice Problems to Drill List
# Comprehension in Your Head.") 
# print('m a h e s h'.count(' '))

# 4) Remove all of the vowels in a string (use string "Practice Problems to Drill List Comprehension 
# in Your Head.")
# print([i for i in 'mahesh' if i in 'aeiou'])

# 5) Find all of the words in a string that are less than 5 letters (use string "Practice Problems to 
# Drill List Comprehension in Your Head.")
# print([word for word in 'This is a programming languages'.split() if len(word) > 5])

# 6) Use a dictionary comprehension to count the length of each word in a sentence (use string 
# "Practice Problems to Drill List Comprehension in Your Head.")
# print({word:len(word) for word in 'This is a programming language'.split() })

# 7) Use a nested list comprehension to find all of the numbers from 1–1000 that are divisible by 
# any single digit besides 1 (2–9)
# print([i for i in range(1, 1000) for j in range(2, 10) if i%j == 0])

# 8) For all the numbers 1–1000, use a nested list/dictionary comprehension to find the highest 
# single digit any of the numbers is divisible by.
# print({num:max([i for i in range(1, 10) if num%i == 0 ]) for num in range(1, 1001)})
