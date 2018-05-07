"""
FIND 33:
Given a list of integers, return True if the array contains a 3 next to a 3 somewhere.
"""
def has_33(nums):
	is_33 = False
	for i in range(len(nums)):
		if i == 0:
			if (nums[i] == 3 and nums[i] == nums[i+1]):
				is_33 = True
				break
			else:
				continue
		if i == (len(nums)-1):
			if (nums[i] == 3 and nums[i] == nums[i-1]):
				is_33 = True
				break
			else:
				continue
		if nums[i] == 3 and (nums[i] == nums[i+1] or nums[i] == nums[i-1]):
			is_33 = True
	return is_33

print("Test #1: {}".format(has_33([1, 3, 3])))
print("Test #2: {}".format(has_33([1, 3, 1, 3])))
print("Test #3: {}".format(has_33([3, 1, 3])))