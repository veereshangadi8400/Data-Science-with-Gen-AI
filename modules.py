# 1. Question 1 
# ○ Create the following modules in the same folder 
# ○ Module 1: string_functions 
# ■ Write a module named string_functions and add the following functions 
# 1. first_word 
# a. Input: string 
# b. Output: first word of the input string 
# 2. last_word 
# a. Input: string 
# b. Output: last word of the input string 
# 3. no_of_words 
# a. Input: string 
# b. Output: number of words in input string 
# ■ Test the above functions by calling them with input as “This is a test string”. 
# Make sure this testing executes only when the program string_functions is 
# executed on its own. Hint: Use __name__ variable. 
# ○ Module 2: string_data  
# ■ Write a module named string_data and add a few variables of type string to it. 
# ○ Module 3: main 
# ■ Now write a module named main that accesses the data present in the 
# string_data and prints the first word, last word and number of words present in 
# each string using the functions in string_functions module. 
# 2. Question 2 
# ○ In Question 1, try all the following to import the modules 
# ■ Import the whole module 
# ■ Rename the module string_functions as sh 
# ■ Import any particular string from string_data using “from”  
# ■ Import all strings from string_data using “from” 
# 3. Question 3 
# ○ In Question 1, try to update the values of strings from string_data to first_word(string). 
# ○ Note your observation, and try to solve this by changing the type of variable. Hint- Use a 
# mutable variable like list to achieve this. 
# 4. Question 4 
# ○ Add a function named printName() in the both modules string_functions and 
# string_data, that prints “string_functions” and “string_data” respectively when called. 
# ○ Import these 2 functions to the module main with the same alias 
# ○ What is the output when printName() is called in the module main 
# 5. Question 5 
# ○ Create 3 different modules named module1, module2, module3 and a function named 
# printSomething() (that prints some statement) to all of these modules. 
# ○ Create a main module and try to import this function from 3 modules using dynamic 
# import and call them.