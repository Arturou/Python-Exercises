"""
Exercises done during big data academy session #3
date: 18/04/2018
Title: Python Basics
"""

#varibles --> dynamic varible type
#variable names shall be lower case and separate words with an underscore
#don't use camel case convention

int_number = 1
float_number = 1.922
bool_var = True
title = "string"

""" 
datatypes:
*integer
*boolean
*strings
*bytes
*list
*tuples
*sets
*dictionaries
"""

"""Exercise #1"""
print("AI-Rocks!")

"""
Exercise #2
Description: string variables
"""
first_name='John'
last_name='Smith'
full_name= first_name +" "+ last_name
print("Hi, my name is {}".format(full_name)) 

"""
Exercise #3
Description: string methods
"""
var = "value"
print(var.upper())
print(var.lower())
print(str(var.count('a')))
print(var.find('va'))
print(var.replace("value","AI-Rocks"))

""" 
Exercise #4
"""
name = input("Enter you age")
print("Your age is {}".format(name))

"""
Exercise #5
get the user's input for two numbers, add and multiply those two numbers
"""
a = input("Enter your first value: ")
b = input("Enter your second value: ")
print("The sum is : {}".format(int(a) + int(b)))
print("The sum is : {}".format(int(a) * int(b)))

"""
Exercise #6
get input from user to calculate the perimeter and area for a rectangle
"""
length = int(input("Length: "))
width = int(input("width: "))
print("Perimeter of rectangle: {}".format((2*length+2*width)))
print("Area of rectangle: {}".format(length*width))