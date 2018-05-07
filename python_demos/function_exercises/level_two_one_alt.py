"""
FIND 33:
Given a list of integers, return True if the array contains a 3 next to a 3 somewhere.
Implementation using regular expression
"""
import re

def has_33(nums):
	nums_as_string = ''.join([str(x) for x in nums])
	return True if re.search( r'33', nums_as_string) else False

print("Test #1: {}".format(has_33([1, 3, 3])))
print("Test #2: {}".format(has_33([1, 3, 1, 3])))
print("Test #3: {}".format(has_33([3, 1, 3])))