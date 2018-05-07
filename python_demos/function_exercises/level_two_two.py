"""
Description: Given a string, return a string where for every character in the original there are three characters
"""
def char_times_three(text):
	#We iterate through each character of our list and multiply it times 3 so we can have 3 times each character.
	result= [(x*3) for x in text] #Single line for is so cool in python!
	#Finally we convert our transformed array of strings into a single string using the join funtion.
	return ''.join(result)
	
print("Test #1: {}".format(char_times_three('Hello')))
print("Test #2: {}".format(char_times_three('Mississippi')))