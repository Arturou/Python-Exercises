"""
SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order.
NOTE: Recursive implementation of the problem.
"""
def spy_game(nums, spy_code):
	curr_num = nums.pop(0)
	if curr_num == spy_code[0]: #checking if current evaluated number is part of spy code pattern
		spy_code.pop(0)
	if len(spy_code) == 1:
		return True #Found spy code pattern
	elif len(nums) != 0:
		return spy_game(nums, spy_code) #Function calling it´s self with modified nums and spy_code
	else:
		return False #Didn´t find spy code pattern
#Optional Testing Code###################################################
"""
Description: Function that validates our output from our custom function
return: A tuple containing a string (Passed or Failed) and our Output
"""	
def test(output, expected_output):
	return "Passed" if output == expected_output else "Failed", output

print("Test #1: {}".format(test(spy_game([1, 2, 4, 0, 0, 7, 5],[0,0,7,"spy!"]), True)))
print("Test #2: {}".format(test(spy_game([1, 0, 2, 4, 0, 5, 7],[0,0,7,"spy!"]), True)))
print("Test #3: {}".format(test(spy_game([1, 7, 2, 0, 4, 5, 0],[0,0,7,"spy!"]), False)))
#Optional Testing Code#####################################################