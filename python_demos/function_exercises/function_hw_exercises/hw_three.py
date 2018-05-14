"""
Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
"""

def check_upper_lower_case(s):
	clean_string = [e for e in s if e.isalpha()]
	upper_case = len([e for e in clean_string if e.isupper()])
	lower_case = len([e for e in clean_string if e.islower()])
	return s, upper_case, lower_case

#Optional Testing Code###################################################
"""
Description: Function that validates our output from our custom function
return: A tuple containing a string (Passed or Failed) and our Output
"""	
def test(output, expected_output):
	compare_outputs = [a == b for a,b in zip(output,expected_output)] #Pair-wise comparison between output and expected_output
	return "Passed" if all(compare_outputs) else "Failed", output #Checking if all item in the list are True and also returning the output

print("Test #1: {}".format(test(check_upper_lower_case("Hello Mr. Rogers, how are you this fine Tuesday?"), ("Hello Mr. Rogers, how are you this fine Tuesday?",4,33))))
print("Test #2: {}".format(test(check_upper_lower_case("Hello Mr. Rogers!"), ("Hello Mr. Rogers!",3,10))))
print("Test #3: {}".format(test(check_upper_lower_case("How are you this fine Tuesday?"), ("How are you this fine Tuesday?",2,22))))
#Optional Testing Code#####################################################