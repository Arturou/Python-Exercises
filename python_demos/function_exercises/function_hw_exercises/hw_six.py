"""
Write a Python function that checks whether a passed in string is palindrome or not.
"""
from functools import reduce
def palindrome(s):
	return s.lower() == s[::-1].lower()

#Optional Testing Code###################################################
"""
Description: Function that validates our output from our custom function
return: A tuple containing a string (Passed or Failed) and our Output
"""	
def test(output, expected_output):
	return "Passed" if output == expected_output else "Failed", output

print("Test #1: {}".format(test(palindrome('helleh'),True)))
print("Test #2: {}".format(test(palindrome('Hello'),False)))
print("Test #3: {}".format(test(palindrome('eye'),True)))
#Optional Testing Code#####################################################