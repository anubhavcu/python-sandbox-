# strings are immutable
name = 'John Doe'
age = 23

print('hello name is ' + name + ' and age is ',  age)
print(' hello world my name is {name} and i am {age} ' .format(
    name=name, age=age))
# use comma when using str and int together in a print statement


# F-string(3.6+)
print(f'Hello world, my name is {name} and age is {age}')


# string methods
# just first letter is capitalized and rest is lower case
print('capitalize', name.capitalize())
new_name = name.capitalize()
print('new name ', new_name)
print(name.replace('Doe', 'williams'))
print(len(name))
sub = 'o'
print(name.count(sub))      # returns the count of variable passed

print(name.startswith('J'))     # true
print(name.startswith('John'))  # true
print(name.startswith('p'))     # false
print('endswith', name.endswith('e'))   # same as startswith
print('endswith', name.endswith('Doe'))

print(name.split())     # splits into a list

print(name.find('D'))
print(name.find('Doe'))   # returns index of character (0-based)
print(name.find('e'))

new_name = 'helloworld'
print(name.isalnum())       # false because of space
# returns true as it checks whether string is either alphabet and numerics only
print(new_name.isalnum())
print('_uew'.isalnum())     # will return false as it has underscore
print(new_name.isalpha())  # true
print(new_name.isnumeric())  # false


# index and slicing of strings
msg = 'new hello world'
print(len(msg))     # range is from -len(str) => len(str) -1 , here -15 to 14
print(msg[0])
# print(msg[16])    # error index out of range
# print(msg[-16])   # index out of range
# msg[2] = 'p'  # error as strings are immutable

print('hello ' * 5)     # prints 5 times
print('hello \n' * 5)   # prints 5 times in new lines
print(msg[-5])
print(msg[-15] == msg[0])

# slicing
print(msg[0:15])  # from 0 to 15-1=14
print(msg[:13])     # from starting to index 12
print(msg[0:])      # from index 0 to end of string
print(msg[:5])
print(msg[-5:])     # 5th position from end(1-based) to end of string

print(msg[:-7])     # from starting to -7-1 = -8 i.e 8th position from the end

print(msg[1:14:2])  # from index 1 to 13 in steps of 2
print(msg[:14:2])   # from starting to index 13 in steps of 2
print(msg[2::2])    # from index 2 to end of string in steps of 2

# -ve steps (when start>end )
print(msg[14: 1: -1])   # from index 14 to 1+1 =2  in reverse direction
# from index 14 to 1+1 =2  in reverse direction in steps of 2
print(msg[14: 1: -2])   # from index 14 to index 1 in steps of 2
print(msg[14:: -1])     # from index 14 to  starting in steps of 1
# note- when we move in negative steps we add (+1) instead of (-1) to end_index

# reversing a string
print(msg[::-1])

new_string = 'the cat sat on the mat'
print("cat" in new_string)  # returns True
print("dog" in new_string)  # false
print('a' in new_string)    # true - can search for characters or words
