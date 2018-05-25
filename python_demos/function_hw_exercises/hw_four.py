"""
Write a Python function that takes a list and returns a new list with unique elements of the first list.
"""

def unique_list(lst):
	return set(lst)

#Optional Testing Code###################################################
"""
Description: Function that validates our output from our custom function
return: A tuple containing a string (Passed or Failed) and our Output
"""	
def test(output, expected_output):
	compare_outputs = [a == b for a,b in zip(output,expected_output)] #Pair-wise comparison between output and expected_output
	return "Passed" if all(compare_outputs) else "Failed", output #Checking if all item in the list are True and also returning the output

print("Test #1: {}".format(test(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]),(1,2,3,4,5))))
print("Test #2: {}".format(test(unique_list([1,1,1,1,2,2,3,]),(1,2,3))))
print("Test #3: {}".format(test(unique_list([5,5,2,2,3,3,3,4,4,4]),(2,3,4,5))))
#Optional Testing Code#####################################################