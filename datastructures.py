"""
With different datatypes
List: dynamic size array
tuples: inmutable  array
sets: unorder unique value array
dictionary: unordered key mapping array
"""

"""Exercise #1"""
mixed = [2, "hi", 1.34]
ages = [10,11,12]
colors = ["red", "yellow", "green"]
list_of_list = [[1,2,3],['one', 'two']]

"""slicing"""
a = [1,2,3,4,5,6,7]

start = 0
end = len(a)-1
step = 2

print('a: {}'.format(a))
print('a: {}'.format(a[2:]))
print('a: {}'.format(a[:-3]))
print('a: {}'.format(a[2:end]))

a.append(8)

"""List methods"""
a.insert(0,10)
a.extend([12,13]) #adds more than one value to list

"""Tuple"""
#takes less memory and reads faster
#inmutable

t = (1,2,3)
print(t[0])
print(t.count(1))
print(t.index(1))

"""set"""
#are like arrays but have unique values
my_set = {1,2,3,3,3,3,3}
print(my_set)
#functions
#add
#update
#remove
#discard
#union
#intersection

a = set([1,2,3,4])
b = set([2,3,4,5])

#a & b
#a < b
#a | b
#a - b

"""Dictionary"""
menu = {}
menu['apple'] = 10.00
menu['mango'] = 12.35
del menu['apple']
print(menu.get('mango'))
print(menu.keys())
print(menu.values())

"""Exercise #2"""
#print values from 1 to 8
ls = [1,4,9,16,25,36,49,64,81,100]
print(ls[2:len(ls)-1:2])

"""Exercise #3"""
"""
add the 5th element to the list "cheetah". Display the number of list items and print the new list
write an assignment statement that will replace the item that currently holds the value "zebra" in zoo_animal list with 'monkey'
remove tiger from the list
"""
zoo_animal = ['elephant', 'zebra', 'tiger', 'lion']
zoo_animal.append('cheetah')
print(zoo_animal)
zoo_animal.pop(zoo_animal.index('zebra'))
zoo_animal.insert(1,'monkey')
print(zoo_animal)
zoo_animal.pop(zoo_animal.index('tiger'))
print(zoo_animal)

"""
with two given list [1,3,6,24,78,35,55] and [12,24,35,88,120,155] write a program to make a list with only the elements that are in both list
"""
a = [1,3,6,24,78,35,55]
b = [12,24,35,88,120,155]
print(a.intersection(b))