"""
Conditionals
"""
X = 5
print(X==5)
print(X==4)

password = "psw"
if password == "psw":
	print("Your cool")
else:
	print("Your not cool")

num = int(input("Enter a number: "))
if num > 10:
	print("Good number")
elif num == 5:
	print("number")
else:
	print("Bad number")

"""Nested If Statement"""
name_emp = input("Insert your name: ")
emp = input("Are you an employee[y/n]: ")
skill_emp = input("Insert your skill[python/java]: ")
if emp.lower() == 'y':
	if skill_emp.lower() == 'python':
		print("Recruiter {}".format(name_emp))
	elif skill_emp.lower() == "java":
		print("You're on hold {}".format(name_emp))
else:
	print("No Vancancy for {}".format(name_emp))

'Hi boss!' if 'arturo' == name_emp.lower() else 'Your not boss!'


"""Loops (iteration)"""
x = 0
while(x < 1000):
	print("This is a virus!!")
	x+=1
print("Finished hacking, bye-bye!")


"""Exercise: Using the while Statement print odd numbers until 10"""
x=0
while(x<10):
	if not (x%2 == 0):
		print(str(x))
	x+=1

"""for loop"""
items = "1,2,3,4,5,6,7"
for item in items:
	print(item)

"""Functions"""
def fun(something):
	print(something)

fun("Hi there :)")

def sum_of_two(a,b):
	return a+b

def super_fun(fun):
	fun(str(fun(a,b)))

fun(str(sum_of_two(10,10)))
super_fun(sum_of_two)

"""Classes and Objects"""
class Human:
	humanCount = 0
	def __init__(self, name, age):
		self.name = name
		self.age = age
		humanCount+=1

	def to_string():
		return "My name is {} and I'm {} years old.".format(self.name, self.age)

	def getCount():
		return humanCount

ace = Human("Ace", 20)
print(ace.to_string())

"""
Best practice
if __name__ == '__main__':
	main()
"""