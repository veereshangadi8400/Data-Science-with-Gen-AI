# Write a Python program using classes, create a class named Vehicle class with 
# max_speed and mileage instance attributes and print attributes by calling with 
# class object.
# class Vehicle:
#     def __init__(self, max_speed, mileage):
#         self.max_speed = max_speed
#         self.mileage = mileage
# bike = Vehicle(120, 30)
# print(bike.mileage, bike.max_speed)
    

# Write a Python program using classes, create a class with the name is circle. Include 
# 1 method named calculate_circle_area which calculates the area of the 
# circle.
# class circle:
#     def calculate_circle_area(r):
#         return 3.14 * r * r
# print(circle.calculate_circle_area(3))

# Write a Python program using classes, create a class with the name is circle. Include 
# 2 methods and 1 constructor which initiates the instance attributes, the methods are 
# named with calculate_circle_area for calculation of its area and another 
# method named calculate_circle_perimeter for calculation of perimeter and 
# asks to user for the radius as the input.
# class circle:
#     def __init__(self, radius):
#         self.radius = radius
#     def calculate_circle_area(self):
#         return 3.14 * self.radius**2
#     def calculate_circle_perimeter(self):
#         return 2 * 3.14 * self.radius
# r = float(input('enter the radius: '))
# c1 = circle(r)
# print(c1.calculate_circle_area())
# print(c1.calculate_circle_perimeter())

# Write a Python program using classes, create a class named is calculator. Which 
# performs the basic arithmetic operations like calculator, without constructor? Add, 
# Subtraction, multiplication, divide all these are the instance 
# methods. 
# variables
class calculator:
    def add(self, a, b):
        return a+b
    def sub(self, a, b):
            return a-b
    def multipy(self, a, b):
            return a*b
    def divide(self, a, b):
        if b == 0:
            return 'Division by zero is not allowed'
        return a/b
cal = calculator()
print(cal.add(4,5))
print(cal.sub(5,4))
print(cal.multipy(4,5))
print(cal.divide(6,3))

# Write a Python program using classes, create a class Employee which initiates 
# instance 
# like 
# emp_department 
# and 
# emp_assign_department, 
# emp_id, 
# methods 
# emp_name, 
# like 
# emp_salary and 
# calculate_emp_salary, 
# and 
# employee_details. 
# Calculate_emp_salary method takes one arguments called hours which is 
# number of hours worked by employee, if employee worked more than 50 hours then 
# salary will b calculated as per the below formula. 
# ot 
# = 
# hours 
# salary = salary + (ot * (salary / 50)) – 
# 50 
# Write a Python program using classes, create a class for banking operations and the 
# class contains constructor to initiates the intake variables, some of the methods 
# named as create_account, despite_amount, withdraw_amount and 
# check_balance. 
# 7. 
# 8. 
# Write 
# a 
# Python program using decorator, create a function called 
# multiply_numbers which accepts the 2 parameters as input and return the value 
# whenever the decorator is called.  
# Write 
# a 
# Python program using decorator, create a function called 
# add_two_numbers and concatenate_two_strings which accepts 2 
# parameters as input. These 2 functions perform the addition operation and 2 
# decorators with type as the parameter for decorator return the value whenever the 
# decorator is called. 
# 9. 
# Write a Python Program ‘Single Inheritance’, Define the Vehicle class which 
# initialize make and model attributes. Define the Car class as a subclass of 
# Vehicle with an additional attribute year. Implement a method detail in both 
# Vehicle and Car classes to print out details such as make, model and 
# year. 
# 10. Write a Python Program using classes, the class has one attribute called c and two 
# instance variables called a, b and has two methods called set_value and 
# get_value. set_value method calculates instance variables and store in c 
# attribute and get_value method will return the value of c. 
# 11. Write a Python program using classes, Create a base class Media which initiates two 
# instance variables title and isPlaying. It has two child classes called 
# AudioPlayer and VideoPlayer. AudioPlayer will initiates two instance 
# variables called title and artist and VideoPlayer will initiates two instance 
# variables called title and director. Each class has methods play() and 
# pause(). play() method will return isPlaying as True and print ‘Playing 
# audio 'Till2 Title Song' by ‘Mika Singh’...‘ similarly pause() 
# method will return as False and print ‘Pausing audio 'Tillu2 Title 
# Song' by ‘Mika Singh’...‘  and same for VideoPlayer class methods. 
# 12. Write a Python program using classes. Create a class called 
# temperature_converter with two static methods called 
# celsius_to_fahrenheit() and fahrenheit_to_celsius(). The 
# celsius_to_fahrenheit() method should convert a temperature from 
# Celsius to Fahrenheit, and the fahrenheit_to_celsius method should 
# convert a temperature from Fahrenheit to Celsius. 
# 13. Write a python program using classes, Create a Python class called 
# trigonometry_calculator that inherits from the calculator class. The 
# calculator class has static methods for basic arithmetic operations like 
# addition, subtraction, multiplication and division. The 
# trigonometry_calculator class to include additional functionality for 
# trigonometric functions like sine, cosine, tangent and an exponential 
# function. 
# 14. Write a python program using classes and encapsulation, Create a class named as 
# Student. The student class has constructor which will initiates private attributes 
# called __name, __marks, write a setter and getter method to get the marks 
# and name. The student class has to calculate the student marks named as 
# calculate_grade and return the pass percentage as given below. 
# a. Consider greater than or equal 90 as Distinction pass. 
# b. Consider greater than or equal 80 as First-class pass. 
# c. Consider greater than or equal 70 as Second-class pass. 
# d. Consider greater than or equal 60 as Third-class pass. 
# e. Consider Below 60 as Fail. 
# 15. Create a Python class Matrix to represent mathematical matrices. Include methods for matrix 
# addition, subtraction, matrix multiplication, and scalar 
# multiplication. Addition method will accept the 2 matrixes as the input perform the 
# addition operation, similar to the subtract method also will perform the subtraction and 
# multiply method will perform the multiplication operation. scalar multiplication 
# method will perform the multiplication with particular number. 
# 16. Create a Python class Car which has constructor, one instance method called start, one 
# nested class called Engine. Engine is a nested class which has one constructor, one instance 
# method called start_engine one nested class called FuelSystem. FuelSystem is 
# another nested class which has one constructor, instance method called inject_fuel. 
# 17. Create a Python class to find the MRO (Method Resolution Order) for the classes. Create class 
# A which has a method called hello, class B which is the child class of class A. Class C which 
# is the child class of A. Class D is the child class of class B and C. Class E is the child class of class C 
# and A. Class F is the child class of class D and E.