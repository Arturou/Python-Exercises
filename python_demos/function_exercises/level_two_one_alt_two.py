"""
FIND 33:
Given a list of integers, return True if the array contains a 3 next to a 3 somewhere.
"""
def has_33(nums):
	for i in range(0,len(nums)-1):
		if nums[i] == 3 and nums[i+1] == 3:
			return True
	return False

print("Test #1: {}".format(has_33([1, 3, 3])))
print("Test #2: {}".format(has_33([1, 3, 1, 3])))
print("Test #3: {}".format(has_33([3, 1, 3])))