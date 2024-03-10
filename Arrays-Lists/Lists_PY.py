# Python Counter is a container that will hold the count of each of the elements present in the container. The counter is a sub-class available inside the dictionary class.
# Counter({'item':'count of item'})

# list1 = ['x','y','z','x','x','x','y', 'z']
# print(Counter(list1))
# Counter({'x': 4, 'y': 2, 'z': 2})

from collections import Counter
a = [12, 3, 4, 3, 5, 11, 12, 6, 7]
x = Counter(a)
print(x)
for i in x.elements():
    print(i)
print(x.keys()) #dict keys
print(x.values()) #dict values
print(list(x.keys()))

#This enumerated object can then be used directly for loops or converted into a list of tuples using the list() function.
#enumerate() function adds a counter as the key of the enumerate object.
#enumerate(iterable,start of the counter)
a = [12, 3, 4, 3, 5, 11, 12, 6, 7]
print(enumerate(a))
print(list(enumerate(a)))
#[(0, 12), (1, 3), (2, 4), (3, 3), (4, 5), (5, 11), (6, 12), (7, 6), (8, 7)]

fruits = ['apple', 'banana', 'cherry']
enum_fruits = enumerate(fruits)
next_element = next(enum_fruits)
print(f"Next Element: {next_element}")
#Next Element: (0, 'apple')

# finding the last occurrence
words = ['eat', 'sleep', 'drink', 'sleep', 'drink', 'sleep', 'go', 'come']
element = 'sleep'
# list comprehension
final_index = max(index for index, item in enumerate(words) if item == element)
#returns a list ----> find max in list
print(final_index)

# The range() function in Python generates a sequence of numbers.
# range(start, stop, step)
numbers = range(8,0,-1)
print(numbers)
# range(8, 0, -1)
# convert to list and print it
print(list(numbers))  
# [8, 7, 6, 5, 4, 3, 2, 1]