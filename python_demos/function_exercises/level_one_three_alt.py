"""
ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
NOTE: Alternative solution to level_one_three.py using abs function.
"""

def almost_there(n):
	return (abs(100-n)<=10) or (abs(200-n)<=10)
	
print("Test #1: {}".format(almost_there(104)))
print("Test #2: {}".format(almost_there(150)))
print("Test #3: {}".format(almost_there(209)))