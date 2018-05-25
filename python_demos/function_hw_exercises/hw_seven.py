"""
Write a Python function to check whether a string is pangram or not.
"""
import string

def ispangram(s, alphabet=string.ascii_lowercase):
	clean_string = "".join([e for e in s if e.isalpha()]) #removing special characters
	compare_input = [e in clean_string for e in alphabet] #checking if our clean string contains all letters of the alphabet
	return all(compare_input)

	
#Optional Testing Code###################################################
"""
Description: Function that validates our output from our custom function
return: A tuple containing a string (Passed or Failed) and our Output
"""	
def test(output, expected_output):
	return "Passed" if output == expected_output else "Failed", output

	
print("Test #1: {}".format(test(ispangram("The quick brown fox jumps over the lazy dog"), True)))
print("Test #2: {}".format(test(ispangram("Hello"), False)))
print("Test #3: {}".format(test(ispangram("eye"), False)))
#Optional Testing Code#####################################################