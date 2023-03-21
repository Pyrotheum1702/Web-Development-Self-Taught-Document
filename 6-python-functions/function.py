# Define function
def sum(a, b):
    result = a + b
    return result

# Call function
number = sum(2, 3)
print(number)
# Result: sum(2 + 3) = 5

number = sum(4, 8)
print(number)
# Result: sum(4 + 8) = 12

# Default argument example
# This function take in 3 different string with default value of "empty" and print them
def print_slot_list(a="empty", b="empty", c="empty"):
    print("A slot = " + a + " B slot = " + b + " C slot = " + c)
    return


# Only pass value to argument a case
print_slot_list("7")
# Only pass value to argument b case
print_slot_list(b="10")
# Only pass value to argument  a and c case
print_slot_list(a="23",c="230")
# Result: A slot = 7 B slot = empty C slot = empty
