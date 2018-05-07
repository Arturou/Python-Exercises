"""
OLD MACDONALD: Write a function that capitalizes 
the first and fourth letters of a name
"""

def old_macdonald(name):
	first = name[0].upper()
	fourth = name[3].upper()
	return first+name[1:3]+fourth+name[4:]
	
print("Test #1: {}".format(old_macdonald('macdonald')))