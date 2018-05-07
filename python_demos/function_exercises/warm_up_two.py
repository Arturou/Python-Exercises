"""
ANIMAL CRACKERS: Write a function that takes a two-word string and 
returns True if both words begin with the same letter
"""

def animal_crackers(text):
	arr = text.split(' ')
	return arr[0][0].lower() == arr[1][0].lower()
	
print("Test #1: {}".format(animal_crackers('Levelheaded Llama')))
print("Test #2: {}".format(animal_crackers('Crazy Kangaroo')))