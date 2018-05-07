"""
MAKES TWENTY: Given two integers, return True if the sum 
of the integers is 20 or if one of the integers is 20. 
If not, return False
"""

def makes_twenty(n1, n2):
	return (n1 + n2) == 20 or (n1 == 20) or (n2 == 20)
	
print("Test #1: {}".format(makes_twenty(20,10)))
print("Test #2: {}".format(makes_twenty(2,3)))