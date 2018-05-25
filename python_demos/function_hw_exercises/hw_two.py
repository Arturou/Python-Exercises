"""
Write a function that checks whether a number is in a given range (inclusive of high and low)
"""

def check_range(num, low, high):
	return num in range(low, high+1)

#Optional Testing Code###################################################
"""
Description: Function that validates our output from our custom function
return: A tuple containing a string (Passed or Failed) and our Output
"""	
def test(output, expected_output):
	return "Passed" if output == expected_output else "Failed", output

print("Test #1: {}".format(test(check_range(5,2,7), True)))
print("Test #2: {}".format(test(check_range(1,3,10), False)))
print("Test #3: {}".format(test(check_range(10,6,10), True)))
#Optional Testing Code#####################################################