class Array:
    def __init__(self, value_list: list):
        self.array = []
        for item in value_list:
            if len(self.array) == 0:
              self.array.append(item)
            else:
                if type(item) != type(self.array[0]):
                    raise TypeError(
                        type(item), ' cannot be interpreted as', type(self.array[0]))
                else:
                    self.array.append(item)

    def __setitem__(self, index: int, value):
        if index < 0 or index >= len(self.array):
            raise IndexError('Index out of bound')
        elif type(value) != type(self.array[0]):
            raise TypeError(
                type(value), ' cannot be interpreted as', type(self.array[0]))
        else:
            self.array[index] = value

    def __getitem__(self, index: int):
        if index < 0 or index >= len(self.array):
            raise IndexError('Index out of bound')
        else:
            return self.array[index]


# Declare an integer array:
arr = Array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Element inspect and type of the elements
print(arr[3])
# Result: arr[3] = 4
print(type(arr[3]))
# Result: type = int

# Declare a float array:
arr = Array([1.1, 2.2, 3.3, 4.4, 5.4, 6.3, 7.2, 8.1, 9.0, 10.0])

# Element inspect and type of the elements
print(arr[3])
# Result: arr[3] = 4.400000095367432
print(type(arr[3]))
# Result: type = float
print(type(arr[9]))
# Result: type = float

# Element has different type to declared type code is invalid.
try:
    arr = Array([1, '2', 3, 4, '2', 6, 7, 8, 9, 10])
except TypeError as error_message:
    print(error_message)
# Result <class 'str'>, ' cannot be interpreted as', <class 'int'>

# Assign value with different data type to array declared datatype is invalid
try:
    arr[5] = 5
except TypeError as error_message:
    print(error_message)
# Result <class 'int'>, ' cannot be interpreted as', <class 'float'>

# Index out of bound.
try:
    arr[-1] = 5.6
except IndexError as error_message:
    print(error_message)
# Result: Index out of bound
