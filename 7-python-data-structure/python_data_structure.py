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
