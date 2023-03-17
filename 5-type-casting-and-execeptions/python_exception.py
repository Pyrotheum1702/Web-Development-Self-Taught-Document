import sys

is_raise_exception_example_on = False

# AssertError Exception example
assert ('win32' in sys.platform), "This program runs on Window 10 only."

# Raise Exception example
if (is_raise_exception_example_on):
    raise Exception("Forced Exception")
# Result: Exception: Forced Exception

# Handling Exception example
try:
    assert ('linux' in sys.platform), "This program runs on Linux only."
except AssertionError as except_message:
    print(except_message)
    print("Exit program...")
# Result: system is not Linux therefore an AssertionError Exception will occur

# 'finally' clause example
try:
    assert ('win32' in sys.platform), "This program runs on Window 10 only."
except AssertionError as except_message:
    print(except_message)
    print("Exit program...")
finally:
    print("this code will be executed in anyway")
# Result: "this code will be executed in anyway"
