"""
MASTER YODA: Given a sentence, return a sentence with the words reversed
"""

def master_yoda(text):
	arr = text.split(' ')
	arr = arr[::-1]
	return ' '.join(arr)
	
print("Test #1: {}".format(master_yoda('I am home')))
print("Test #2 {}".format(master_yoda('We are ready')))