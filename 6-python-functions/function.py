
# Define function
def sum(a, b):
    result = a + b
    return (result)


# Call function
number = sum(2, 3)
print(number)
# Result: sum(2 + 3) = 5

number = sum(4, 8)
print(number)
# Result: sum(4 + 8) = 12

# Default argument example


def print_slot_list(a="empty", b="empty", c="empty"):
    print("A slot = " + a + " B slot = " + b + " C slot = " + c)
    return


print_slot_list("7")
# Result: A slot = 7 B slot = empty C slot = empty
