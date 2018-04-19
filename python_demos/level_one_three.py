"""
ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
"""

def almost_there(n):
	return (n >= 90 and n<=110) or (n >= 190 and n<=210)
	
print("Test #1: {}".format(almost_there(104)))
print("Test #2: {}".format(almost_there(150)))
print("Test #3: {}".format(almost_there(209)))