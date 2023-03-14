#


# Python basic Variable types
# There are multiple built-in data types
# but in this document i will focus on these basic type of variable:
# Integer | Float | String

# variable declare syntax
# variable name | = | value
# in Python 3.x int values are unlimited in size (im not really sure about this)
number = 1000  # integer, numeric number

string = "im a string"  # text, use " " or ' ' work the same

pi_number = 3.14  # float, decimal number
# in Python, type of the variable is determined by it's value
number = "1000"
# since var *number* was an integer now it's a string
number = 1001
# it's integer once again..

# a variable is a reference or a pointer to an object
# example: number -------> [1001]
# explanation: number is pointing to an integer object with a value of 1001
# so with the following statement:
number_1 = number
# number_1 will also point to integer object with value of 1001
# number -------> [1001] <----- number1

# notice: a variable does not work exactly like a pointer
# consider this statement:
number = 999
# number is now point to a new integer object
# number -----> [999]
# number_1 ---> [1001]

# if an object is orphaned(no reference) it will automatically get deleted by garbage collection
number_1 = 1000
# number ----> [999]
# number_1 --> [1000]
#  ?     ----> [1001] orphaned
