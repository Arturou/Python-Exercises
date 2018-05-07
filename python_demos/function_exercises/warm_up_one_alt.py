""" 
LESSER OF TWO EVENS: Write a function that returns the lesser of 
two given numbers if both numbers are even, but returns the greater
if one or both numbers are odd
NOTE:Alternative solution to warmup_one.py without using nested  if else statements.
"""

def lesser_of_two_evens(a,b):
	if a % 2 == 0 and b % 2 == 0:
		return min(a,b) #we can use min() function to bring the smallest number
	else:
		return max(a,b) #we can use max() function to bring the biggest number

print("Test #1: {}".format(lesser_of_two_evens(2,4)))
print("Test #2: {}".format(lesser_of_two_evens(2,5)))