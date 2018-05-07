"""
OLD MACDONALD: Write a function that capitalizes 
the first and fourth letters of a name
"""

def old_macdonald(name):
	return name[:3].capitalize()+name[3:].capitalize()
	
print("Test #1: {}".format(old_macdonald('macdonald')))