numbers = [1, 2, 4, 2, 53, 43, 11, 34, 64]

for number in numbers:
    print(number)

for x in range(10):
    if x == 9:
        break

    if x == 5:
        continue
    print(x)

# for indices

for x in range(len(numbers)):
    print('h', x, numbers[x])

# range
# range(start, stop, step) , default step is 1, steps can be +ve or -ve but not 0

# for x in range(1, 11):
#     print(x, end=' ')

# for x in range(1, 100, 10):
#     print(x, end=' ')

# decrementing with range

for x in range(10, 2, -2):  # same, doesn't go upto 2
    print('reverse', x)

# reversed

for x in range(10, 0, -1):      # from 10 to 1
    print('-ve index ', x)

for x in reversed(range(11)):  # from 10 to 1
    print('reversed range', x)

print('len of array', len(numbers))

for x in reversed(range(len(numbers))):  # len(array) = 9, so we get x from 8 to 0
    print(x)

for x in range(10):  # 0 to 9
    print(x)


# while loops
count = 0

while count <= 10:
    print(f'Count: {count}')
    count += 1


# zip - used for looping over multiple lists at same time
l1 = [1, 2, 3, 4, 5, 6]
l2 = ['a', 'b', 'c', 'd', 'e', 'f']

for a, b in zip(l1, l2):
    print(a, b)

# enumerate is used to iterate a list while keeping track of indices
# if we used regular loop like- for i in range(new_list): print(new_list[i]) ,enumerate basically provides an alternative
new_list = [12, 3, 2, 1, 32, 4, 4, 3, 65, 32]

for num, line in enumerate(new_list):
    print('enumerate',  num, line)
