import math
# This file only use object oriented programming paradigm

# In this file a Calculator object will do everything with it's data and methods
class Calculator:
    def __init__(self):
      self.current_value = 0

    def add(self, value: float):
      self.current_value += value

    def subtract(self, value: float):
      self.current_value -= value

    def multiply(self, value: float):
      self.current_value *= value

    def divide(self, value: float):
      self.current_value /= value

    def calculate_square_root(self):
      self.current_value = math.sqrt(self.current_value)

    def calculate_exponent(self, value):
      self.current_value **= value

    def print_current_value(self):
      print(self.current_value)

cal = Calculator()

# Test section:
cal.add(5)
cal.print_current_value()
# Result: cal.current_value = 5

cal.add(3)
cal.print_current_value()
# Result: cal.current_value = 8

cal.subtract(4)
cal.print_current_value()
# Result: cal.current_value = 4

cal.multiply(8)
cal.print_current_value()
# Result: cal.current_value = 32

cal.divide(2)
cal.print_current_value()
# Result: cal.current_value = 16

cal.calculate_square_root()
cal.print_current_value()
# Result: cal.current_value = 4

cal.calculate_exponent(5)
cal.print_current_value()
# Result: cal.current_value = 1024