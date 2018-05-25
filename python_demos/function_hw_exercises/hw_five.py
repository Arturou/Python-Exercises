"""
Write a Python function to multiply all the numbers in a list.
"""
from functools import reduce
def multiply(nums):
	return reduce((lambda curr, next: curr*next),nums)

#Optional Testing Code###################################################
"""
Description: Function that validates our output from our custom function
return: A tuple containing a string (Passed or Failed) and our Output
"""	
def test(output, expected_output):
	return "Passed" if output == expected_output else "Failed", output

print("Test #1: {}".format(test(multiply([1, 2, 3, -4]),-24)))
print("Test #2: {}".format(test(multiply([1, -20, 3, -4]),240)))
print("Test #3: {}".format(test(multiply([1, 2, 30, 40]),2400)))
#Optional Testing Code#####################################################