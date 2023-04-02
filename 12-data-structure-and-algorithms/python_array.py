class Array:
    def __init__(self, data_type: str, value_list: list):
        match data_type:
            case 'b':
                self.data_type = int
            case 'B':
                self.data_type = int
            case 'u':
                self.data_type = int
            case 'h':
                self.data_type = int
            case 'H':
                self.data_type = int
            case 'i':
                self.data_type = int
            case 'I':
                self.data_type = int
            case 'l':
                self.data_type = int
            case 'L':
                self.data_type = int
            case 'q':
                self.data_type = int
            case 'Q':
                self.data_type = int
            case 'f':
                self.data_type = float
            case 'd':
                self.data_type = float
            case _:
                raise TypeError('unexpected type')

        self.array = []
        for item in value_list:
            if type(item) != self.data_type:
                raise TypeError(
                    type(item), ' cannot be interpreted as', self.data_type)
            else:
                self.array.append(item)

    def __setitem__(self, index: int, value):
        if index < 0 or index >= len(self.array):
            raise IndexError('Index out of bound')
        elif type(value) != self.data_type:
            raise TypeError(
                type(value), ' cannot be interpreted as', self.data_type)
        else:
            self.array[index] = value

    def __getitem__(self, index: int):
        if index < 0 or index >= len(self.array):
            raise IndexError('Index out of bound')
        else:
            return self.array[index]


# Declare an integer array:
arr = Array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Element inspect and type of the elements
print(arr[3])
# Result: arr[3] = 4
print(type(arr[3]))
# Result: type = int

# Declare a float array:
arr = Array('f', [1.1, 2.2, 3.3, 4.4, 5.4, 6.3, 7.2, 8.1, 9.0, 10.0])

# Element inspect and type of the elements
print(arr[3])
# Result: arr[3] = 4.400000095367432
print(type(arr[3]))
# Result: type = float
print(type(arr[9]))
# Result: type = float

# Element has different type to declared type code is invalid.
try:
    arr = Array('i', [1, '2', 3, 4, '2', 6, 7, 8, 9, 10])
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
except TypeError as error_message:
    print(error_message)
# Result <class 'int'>, ' cannot be interpreted as', <class 'float'>
