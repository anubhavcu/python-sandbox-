# lists are ordered and mutable sequence , allows duplicate members
# lists are also heterogenous (can contain int, float,str type together)

import random
numbers = [1, 2, 3, 4, 5, 6]
# numbers1 = list(1, 2, 3, 4, 5)   # will generate an error - as list constructor takes 1 argument only
numbers1 = list((1, 2, 3, 4, 5))
heterogenous_list = [1, 2, 3, 4, 'abc']
print(heterogenous_list)

print('lists on new line ', numbers, '\n', numbers1)

fruits = ['apple', 'oranges', 'grapes', 'pears']
print(len(fruits))
print(fruits[1])

# adding to list
fruits.append('mangoes')
print(fruits)

# adding to position
fruits.insert(3, 'banana')
print(fruits)
l1 = [1, 2, 3, 4]
l1.insert(2, [7, 8])
print('inserting a list ', l1)

# remove elements
fruits.remove('pears')
print(fruits)

# remove with pop
fruits.pop(3)
fruits.pop()    # removes last element if no index is provided
print(fruits)

# reverse
fruits.reverse()
print(fruits)

# sorting
fruits.append('aa')
fruits.sort()
print(fruits)

# reverse sort
fruits.sort(reverse=True)
print(fruits)

# changing values
fruits[1] = 'changed value'
fruits[len(fruits)-1] = 'blueberries'
print(fruits)

# some more eg

a = [1, 2, 3, 'cat']   # heteregenous list
print(len(a))
print(a[-1])
print(a[1])


# * can be used to create multiple concatenated copies of list
a = a * 2
print('multiply', a)

# in can be used to check for membership ( same as with strings)
print('cat' in a)   # return true
print(3 in a)       # true
print(4 in a)       # false

list1, list2 = [1, 2, 3, 4], [5, 6, 7, 8]
print(list1, list2)
# we can use '+' to concatenate two lists
list3 = list1 + list2
print('concatenate two strings ', list1+list2)
print(list3)

print(a)
print(a.index('cat'))   # returns the first occurence of the searched element
print(a.index(2))
print(a.count('cat'))

random_list = [1, 2, 3]
print(random_list)
random_list[0] = 2

print(random_list)
print(random_list[-1] == random_list[len(random_list) - 1])

# unpacking of list elements  - make sure to use correct number of parameters on both sides
new_list = [1, 2, 3]
a, b, c = new_list

print(a, b, c)
# d, e, f = [1, 2], 15    # will throw an error- either use complete list with exact number of values in list to number of variables value is being assigned to.
# d, e, f = [1, 2, 3, 4]      # throw an error  - too many values to unpack
d, e, f = [10, 20, 30]
print(d, e, f)
# eg
x = [1, 2, 3, 4]
y = [10, 20, x, 30]
z = [10, 20, *x, 30]
print('embedding a list', y)
print('unpacking a list ', z)


# swapping lists
l1 = [1, 2, 3]
l2 = [5, 6, 7]

print('l1', l1)
print('l2', l2)

l1, l2 = l2, l1

print('l1', l1)
print('l2', l2)

# slicing of lists, same as with strings
numbers_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers_list[:5])
print(numbers_list[:: -1])      # reversed list

# to check if present
print(8 in numbers_list)

# list of lists
a = [1, 3, 5, 7, 9]
b = [2, 4, 6, 8, 10]
c = [a, b]
print(c)
# 0th element of 0th list and element with index 2 of list with index 1
print(c[0][0], c[1][2])

# list comprehension
p = [random.randint(10, 100) for n in range(20)]
print(p)


l1 = [1, 2, 3, 4, 5]
l1 = l1[::-1]
# print(l1[::-1])
print(l1)
