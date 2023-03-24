fruits = ['orange', 'apple', 'pear', 'banana']

# List Data Structure

# Create a list example:
list_1 = [1, 2.0, "three"]
print(list_1)
# Result: list_1 = [1, 2.0, "three"]

# Create a list using the list() constructor
list_2 = list([1, 2.0, "three", 4])
print(list_2)
# Result: list_1 = [1, 2.0, "three", 4]

# List index accessing example:
list_3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_3[0])
# Result: list_3[0] = 1
print(list_3[-1])
# Result: list_3[-1] = 10
print(list_3[3])
# Result: list_3[3] = 4
print(list_3[-4])
# Result: list_3[-4] = 7
print(list_3[2:3])

# If the given index is higher than the size of the list example no.1:
try:
    print(list_3[13])
except Exception as error_message:
    print(error_message)
    print("Exception type: ", type(error_message))
# Result: list index out of range
# Exception type: IndexError

# If the given index is higher than the size of the list example no.2:
try:
    print(list_3[-12])
except Exception as error_message:
    print(error_message)
    print("Exception type: ", type(error_message))
# Result: list index out of range
# Exception type: IndexError

# Multiple data type in a list example
abc = ["string", 12, 93.4]
print(abc)
# Result: abc = ['string', 12, 93.4]

# Slicing list example:

number_list = [0,1,2,3,4,5,6,7,8,9,10]

# `list[:]` example:
print(number_list[:])
# Result: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# `list[x:]` example:
print(number_list[4:])
# Result: [4, 5, 6, 7, 8, 9, 10]

# `list[:x]` return a new  list form start of the list to index `x` - 1
print(number_list[:8])
# Result: [0, 1, 2, 3, 4, 5, 6, 7]

# `list[x:y]` return a new  list from index `x` to index `y` - 1
print(number_list[3:9])
# Result: [3, 4, 5, 6, 7, 8]

# `list[x:y:z]` return a new  list from index `x` to index `y` - 1 by `z` step between each element
print(number_list[0:11:1])
# Result: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(number_list[0:11:2])
# Result: [0, 2, 4, 6, 8, 10]
print(number_list[0:-1:3])
# Result: [0, 3, 6, 9]
print(number_list[-10:-1:2])
# Result: [1, 3, 5, 7, 9]
print(number_list[1:10:2])
# Result: [1, 3, 5, 7, 9]

# All use of list methods example:

# `list.append` example:
fruits.append('grape')
print(fruits)
# Result: fruits = ['orange', 'apple', 'pear', 'banana', 'grape']

# `list.extend` example:
fruits.extend(['kiwi', 'apple', 'banana'])
print(fruits)
# Result: fruits = ['orange', 'apple', 'pear', 'banana', 'grape', 'kiwi', 'apple', 'banana']

# `list.insert(i, x)` example:
fruits.insert(2, "strawberry")
print(fruits)
# Result: fruits = ['orange', 'apple', 'strawberry', 'pear', 'banana', 'grape', 'kiwi', 'apple', 'banana']

# `list.remove` example:
fruits.remove("pear")
print(fruits)
# Result: fruits = ['orange', 'apple', 'strawberry', 'banana', 'grape', 'kiwi', 'apple', 'banana']

# `list.remove(x)` if `x` is not in list example:
try:
    fruits.remove("watermelon")
except Exception as error_message:
    print(error_message)
    print("Exception type: ", type(error_message))
# Result: watermelon is not in fruits
# Exception type: ValueError

# `list.pop()` example:
popped_element = fruits.pop()
print("popped element: ", popped_element)

# `list.pop(x)` example:
popped_element = fruits.pop(4)
print("popped element: ", popped_element)

# fruits list after pop methods
print(fruits)
# Result: fruits = ['orange', 'apple', 'strawberry', 'banana', 'kiwi', 'apple']

# `list.clear` example:
fruits.clear()
print(fruits)
# Result: fruits = []


# Set Data Structure

# Create a set using curly brackets
set_1 = {1, 2, 3}
print(set_1)
# Result: set_1 = {1, 2, 3}

# Create a set using the `set()` constructor
set_2 = set([1, 2, 3, 4])
print(set_2)
# Result: set_2 = {1, 2, 3, 4}

# Set Union Method

set_1 = {1,2,3,4,5,6,7,8}
set_2 = {4,5,6,7,8,9,10}

# Set union method example:
print(set_1.union(set_2))
# Result: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# Set union method with a tuple example:
print(set_1.union((10,11,12,18,19,20)))
# Result: {1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 18, 19, 20}

# Set union method with a list example:
print(set_1.union([-10,-11,-12,18,19,20]))
# Result: {1, 2, 3, 4, 5, 6, 7, 8, 18, 19, -12, -11, -10, 20}

# Set union operator example:
print(set_1 | set_2)
# Result: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# Set union operator with other iterable type example:
try:
    print(set_1 | (60,61,62))
except Exception as error_message:
    print(error_message)
    print("Exception type: ", type(error_message))
# Result: unsupported operand type(s) for |: 'set' and 'tuple'
# Exception type: TypeError

# Set intersection Method

set_1 = {1,2,3,4,5,6,7,8}
set_2 = {4,5,6,7,8,9,10}

# Set intersection method example:
print(set_1.intersection(set_2))
# Result: {4, 5, 6, 7, 8}


# Set intersection operator example:
print(set_1 & set_2)
# Result: {4, 5, 6, 7, 8}

# Set more than 2 intersection operator example:
print(set_1 & set_2 & {5,6,7})
# Result: {5, 6, 7}
print(set_1 & set_2 & {1,2,3,5,6,7,10} & {1,5,6,8,10,14})
# Result: {5, 6}


# Set difference Method

set_1 = {1,2,3,4,5,6,7,8}
set_2 = {4,5,6,7,8,9,10}

# Set difference method example:
print(set_1.difference(set_2))
# Result: {4, 5, 6, 7, 8}


# Set difference operator example:
print(set_1 - set_2)
# Result: {1, 2, 3}

# Set more than 2 difference operator example:
print(set_1 - set_2 - {1,3,4,5})
# Result: {2}
print(set_1 - set_2 - {3,5} - {1,-1})
# Result: {2}

# Dictionary Data Structure

# Create a dictionary using curly brackets
dict_1 = {"one": 1, "four": 4, "two": 2}
print(dict_1)
# Result: dict_1 = {1, 2, 3}

# Create a dictionary using the `dict()` constructor
dict_2 = dict([["one", 1], ["four", 4], ["nine", 9], ["two", 2]])
print(dict_2)
# Result: dict_2 = {'one': 1, 'four': 4, 'nine': 9, 'two': 2}

# Get a value from a key in a dictionary
print(dict_2["two"])
# Result: dict_2["two"] = 2

# Dictionary Methods

d = {"Duoc": "Tu Son",
     "Dat": "Luong Tai",
     "Tam": "Hiep Hoa",
     "Hieu": "Luc Ngan",
     "Hung": "Lang Giang"
}

d_2 = {"Duoc": "Ha Noi",
     "Hiep": "Tu Son",
     "Tam": "Hiep Hoa",
     "Long": "Que Vo",
}

# .get(x) method example:
print(d.get("Dat"))
# Result: Luong Tai
print(d.get("Dung"))
# Result: None

# .get(x, y) method example:
print(d.get("Hieu", "Ten khong ton tai"))
# Result: Luc Ngan
print(d.get("Hiep", "Ten khong ton tai"))
# Result: Ten khong ton tai

# .items() method example:
print(d.items())
# Result: dict_items([('Duoc', 'Tu Son'),
#                     ('Dat', 'Luong Tai'),
#                     ('Tam', 'Hiep Hoa'),
#                     ('Hieu', 'Luc Ngan'),
#                     ('Hung', 'Lang Giang')])

# .keys() method example:
print(d.keys())
# Result: dict_keys(['Duoc', 'Dat', 'Tam', 'Hieu', 'Hung'])

# .values() method example:
print(d.values())
# Result: dict_values(['Tu Son', 'Luong Tai', 'Hiep Hoa', 'Luc Ngan', 'Lang Giang'])

# .pop(x) method example:
user_name = "Tam"
print("Huyen cua " + user_name + " =", d.pop(user_name))
# Result: Huyen cua Tam = Hiep Hoa

# .pop(x, y) method example:
user_name = "Tam"
print("Huyen cua " + user_name + " =", d.pop(user_name, "Khong ton tai"))
# Result: Huyen cua Tam = Ten khong ton tai

# .popitem() method example:
print("popped element =",d.popitem())
# Result: popped element = ('Hung', 'Lang Giang')

# d and d_2 before the .update() method
print(d)
# Result d = { 'Duoc': 'Tu Son',
#              'Dat': 'Luong Tai',
#              'Hieu': 'Luc Ngan'}
print(d_2)
# Result d = { 'Duoc': 'Ha Noi',
#              'Hiep': 'Tu Son',
#              'Tam': 'Hiep Hoa',
#              'Long': 'Que Vo'}

# .update(x) method example:
d.update(d_2)
print(d)
# Result d = { 'Duoc': 'Ha Noi',
#              'Dat': 'Luong Tai',
#              'Hieu': 'Luc Ngan',
#              'Hiep': 'Tu Son',
#              'Tam': 'Hiep Hoa',
#              'Long': 'Que Vo'}

# .clear()`: Clear all keys and values from the dict.
d.clear()
print(d)
# Result: d = {}

# Tuple Data Structure

# Create a tuple using round brackets
tuple_1 = (1, 2, 3, 4)
print(tuple_1)
# Result: tuple_1 = (1, 2, 3, 4)

# Create a tuple from a list the tuple() constructor
tuple_2 = tuple([1, 2, 3, 4, 5])
print(tuple_2)
# Result: tuple_2 = (1, 2, 3, 4, 5)

# If you change the value of a tuple example:
try:
    tuple_1[1] = 3
except Exception as error_message:
    print(error_message)
    print("Exception type: ", type(error_message))
# Result: 'tuple' object does not support item assignment
# Exception type: TypeError
