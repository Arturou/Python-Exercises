"""
SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers 
starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
"""
def summer_69(arr):
	arr_sum = 0
	found_6 = False
	for num in arr:	
		if num == 6 and not found_6:
			found_6 = True
			continue
		elif num == 9 and found_6:
			found_6 = False
			continue
		if not found_6:
			arr_sum+=num
	return arr_sum

#Optional Testing Code###################################################
"""
Description: Function that validates our output from our custom function
return: A tuple containing a string (Passed or Failed) and our Output
"""	
def test(output, expected_output):
	return "Passed" if output == expected_output else "Failed", output

print("Test #1: {}".format(test(summer_69([1, 3, 5]), 9)))
print("Test #2: {}".format(test(summer_69([4, 5, 6, 7, 8, 9]), 9)))
print("Test #3: {}".format(test(summer_69([2, 1, 6, 9, 11]), 14)))
#Optional Testing Code#####################################################