""" 
Create a fucntion that returns an int given a string representation of an int.
"""
import sys
import functools

def parseInt(s):
	"""
	@func: Function that converts a string representation of a number to an integer.
	@param: s A string of representation of an integer number
	@return: Integer number representation of the input string
	"""
	max_pow_int = len(str(sys.maxsize))-1
	string_to_num = {"0":0, "1":1, "2":2, "3":3,  "4":4, "5":5, "6":6, "7":7, "8":8, "9":9}
	if not s.isdigit():
		return "The given string is not a number"
	if len(s)-1 > max_pow_int:
		return "The converted value is to big to be stored as an int variable"
	arr_nums = [string_to_num[e] for e in s]
	arr_nums = arr_nums[::-1]
	arr_nums = [value*10**index for index, value in enumerate(arr_nums)]
	return functools.reduce(lambda accu, next: accu+next, arr_nums)

print(str(parseInt("12341234567")))