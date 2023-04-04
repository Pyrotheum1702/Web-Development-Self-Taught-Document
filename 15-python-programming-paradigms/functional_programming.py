import math
# This file only use functional programming paradigm

# In this file only functions will be used to perform calculations

# Pure function
def add(value_1: float, value_2: float):
  return value_1 + value_2

# Pure function
def subtract(value_1: float, value_2: float):
  return value_1 - value_2

# Pure function
def multiply(value_1: float, value_2: float):
  return value_1 * value_2

# Pure function
def divide(value_1: float, value_2: float):
  return value_1 / value_2

# Pure function
def calculate_square_root(value):
  return math.sqrt(value)

# Pure function
def calculate_exponent(value_1: float, value_2: float):
  return value_1 ** value_2

number = 0
# Test section:
number = add(number, 5)
print(number)
# Result: number = 5

number = add(number, 3)
print(number)
# Result: number = 8

number = subtract(number, 4)
print(number)
# Result: number = 4

number = multiply(number, 8)
print(number)
# Result: number = 32

number = divide(number, 2)
print(number)
# Result: number = 16

number = calculate_square_root(number)
print(number)
# Result: number = 4

number = calculate_exponent(number, 5)
print(number)
# Result: number = 1024