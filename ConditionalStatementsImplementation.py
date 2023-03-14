
# Python Conditional Statements
# in this document i will not explain how conditional statement works
# because i already know how they generally work in most languages
# but i will talk about how to implement them and if they work differently.


# *if* statement
''' prototype
if <boolean>:
    <statements>
'''
# ---------------------------#
if (True):
    print("the condition is true")
# ---------------------------#
# in Python program contiguous statements that's are in the same column
# are considered to be a part of the same block

''' prototype
if <boolean>:
    <statements>
    <statements>
    <statements>
'''
# ---------------------------#
if (False):
    print("the condition is true")  # will not execute
    print("the condition is true")  # will not execute
    print("the condition is true")  # will not execute
print("hello_world")  # will execute anyway
# ---------------------------#
# *else* statement
''' prototype
if <boolean>:
    <statements>
else:
    <statements>
'''
# ---------------------------#
if (False):
    print("the condition is true")
else:
    print("the condition is false")
# ---------------------------#
# *elif* statement
# basically else + if
''' prototype
if <boolean>:
    <statements>
elif <boolean>:
    <statements>
'''
# ---------------------------#
test_score = 4  # 0-10
if (test_score >= 8):
    print("Grade = A")
elif (test_score < 5):
    print("Grade = C")
else:
    print("Grade = B")
# ---------------------------#
# one line conditional statement also work, but dont code like this!
'''
if test_score >= 5 : print("exam passed")
else : print("exam failed")
'''

# Conditional Expression
# or Ternary operator

'''
<statement1> if <boolean> else <statement2>
'''
# ---------------------------#
test_score = 6  # 0-10
print("exam", "passed" if test_score >= 5 else "failed")
is_pass_exam = True if test_score >= 5 else False
is_pass_exam = test_score >= 5  # same result as above
# ---------------------------#
