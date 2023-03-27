from array import array

# Declare an integer array:
arr = array('i', [1,2,3,4,5,6,7,8,9,10])

# Element inspect and type of the elements
print(arr[3])
# Result: arr[3] = 4
print(type(arr[3]))
# Result: type = int

# Declare a float array:
arr = array('f', [1.1,2.2,3.3,4.4,5.4,6.3,7.2,8.1,9.0,10])

# Element inspect and type of the elements
print(arr[3])
# Result: arr[3] = 4.400000095367432
print(type(arr[3]))
# Result: type = float
print(type(arr[9]))
# Result: type = float

# Element has different type to declared type code is invalid.
try:
  arr = array('i', [1,'2',3,4,'2',6,7,8,9,10])
except Exception as error_message:
  print(error_message)
# Result 'str' object cannot be interpreted as an integer
