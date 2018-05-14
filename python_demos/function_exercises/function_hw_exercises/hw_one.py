"""
Write a function that computes the volume of a sphere given its radius.
NOTE: V = (3/4)*PI*r^3
"""
from math import pi
def vol(rad):
	return (3/4) * pi * (rad**3)

#Optional Testing Code###################################################
"""
Description: Function that validates our output from our custom function
return: A tuple containing a string (Passed or Failed) and our Output
"""	
def test(output, expected_output):
	return "Passed" if output == expected_output else "Failed", output

print("Test #1: {}".format(test(vol(2), 18.84955592153876)))
print("Test #2: {}".format(test(vol(4), 150.79644737231007)))
print("Test #3: {}".format(test(vol(8), 1206.3715789784806)))
#Optional Testing Code#####################################################