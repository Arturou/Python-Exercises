#how to install scala IDE eclipse in cloudera quickstart
#install scala IDE in windows or ubuntu
"""Data Structures"""
x = "Hello World"
o = 0
l = 0
for item in x:
	if item.lower() == "o":
		o+=1
	elif item.lower() == "l":
		l+=1

print("The number of 'o': {}".format(o))
print("The number of 'l': {}".format(l))
print("The total sum: {}".format(o+l))

"""Date and Time manipulation"""
from datetime import date

today = date.today()
today.day
today.month
today.year
today.weekday

now = datetime.now()

t = dateyime.time(now)
t.hour
t.minute
t.second
t.microsecond
t.tzinfo