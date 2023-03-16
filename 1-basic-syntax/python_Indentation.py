
# 1. What is indentation
#   - Example:
if (True):
    print("A")
# ^ |
# |
# This part with spaces is indentation
# --------------------------------------------------
# 2. How multiple line is considered a code block?
#   - Lines with equal amount of indentation are considered a code block
#   - Example:
#    - Read the code from below, there are 4 print() function call, i separate them by A B C D
if (True):
    print("A")  # A - belong to code block 1
    print("B")  # B - belong to code block 1
    if (False):  # - belong to code block 1
        print("C")  # C - belong to code block 2
    print("D")  # D - belong to code block 1

#     -Explanation: Only A B and D would get executed, C would'nt
# because it has different amount of spaces at the start of the line
# therefore it's not in the same code block as A B and D. Instead
# it's belong to the second if statement which it's condition is false.

#     -Notice: D print() function call separated by 1 line but
# it's still considered belong to code block 1 because it's has
# equal amount of spaces at start with A and B.
