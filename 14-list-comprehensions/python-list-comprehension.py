import math

# List comprehension example:

# Simple example:

n = 13
# Consider this process of creating a list containing numbers from 1 to `n` using for loop
list_1 = []
for i in range(n):
    list_1.append(i+1)

print(list_1)
# Result: list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# The process above could be compress down to a single line of code using list comprehension
list_2 = [i+1 for i in range(n)]
print(list_2)
# Result: list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

#-------------

# Deeper example:

n = 36
# Consider this process of creating a list containing numbers from 1 to `n` where if the number is a square value of any number,
# it would be kept as number else it would be `.` using for loop
list_3 = []
for i in range(1, n+1):
  if float(math.sqrt(i)).is_integer():
    list_3.append(i)
  else:
    list_3.append('.')

print(list_3)
# Result: list_3 = [1, '.', '.', 4, '.', '.', '.', '.', 9, '.', '.', '.', '.', '.', '.', 16,
# '.', '.', '.', '.', '.', '.', '.', '.', 25, '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 36]

# The process above could be compress down to a single line of code using list comprehension
list_3 = [i if float(math.sqrt(i)).is_integer() else '.' for i in range(1, n+1)]
print(list_3)
# Result: list_3 = [1, '.', '.', 4, '.', '.', '.', '.', 9, '.', '.', '.', '.', '.', '.', 16,
# '.', '.', '.', '.', '.', '.', '.', '.', 25, '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 36]