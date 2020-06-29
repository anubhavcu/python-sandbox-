# # ways for taking input

# # single input
# # strings
# name = input('enter name ')

# print(name, type(name))

# # int
# number = int(input('enter any number : '))
# print('You have entered : ', number)
# # float
# balance = float(input('enter balance :'))
# print('balance is ', balance)


# # -----------
# # taking known number of inputs
# m, n = map(int, input('enter two numbers, space seperated  ').split())
# # can also pass space or comma as parameter in split funtion

# print(m, n)


# # -----------
# # taking variable number of inputs
# # strings
# l = list(input('enter a sentence ').split())
# # eg- i/p = hello world,  o/p -  ['hello', 'world']
# print(l)


# # int
# l = list(map(int, input('enter numbers space seperated  ').split()))
# print(l)

# we can also use set or tuples instead of lists


# ----------------output
l1 = [1, 2, 3, 4, 5]

for l in l1:
    print(l)    # prints in new line

for l in l1:
    print(l, end=' ')  # prints in same line

# more eg
res = [21, 34, 32, 45, 65, 53]

for i in range(len(res)):
    # print('Case #{x}:'.format(x=i+1), res[i])
    print('Case #{}:'.format(i+1), res[i])
# we don't need to pass values in placeholder({}) if there is only one variable

# alternative approach to above is using enumeraters

for i, v in enumerate(res):
    print('Case #{}:'.format(i), v)
