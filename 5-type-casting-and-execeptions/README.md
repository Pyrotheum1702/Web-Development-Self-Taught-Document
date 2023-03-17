# Content Overview
  1. Python Typecast
  2. Python Exceptions

# Python Typecast
  1. Lesson content:
  - What is type casting
  - Implicit Type Casting
  - Explicit Type Casting
  2. What i learned:
  - Type casting is a method to convert value of a data type to another data type
  - Implicit type casting is type casting automatically perform by Python
    - Example : if you perform a calculation with an integer to a float the result would be a float value
  - Python can not perform a addition with a string to an int or a float automatically so you need to use explicit Type Casting method to do it
  - Mainly in explicit type casting can be done with these data type function:
    - `int()` function take float or string as an argument and return int type object
    - `str()` function take float or int as an argument and return string type object
    - `float()`function take int or string as an argument and return float type object

# Python Exception
  1. Lesson content:
  - What is an exception
  - Raising an exception
  - AssertionError exception
  - Handling Exceptions
  2. What i learned:
  - An Exception is an error that happens during the execution of a program. Whenever there is an error, Python generates an exception that could be handled
  - Use `raise exception` to force a specified exception to occur.
  - Use `assert (condition, error message)` for AssertionError exception. If the condition is met, the program will continue , else the program will stop and throw an AssertionError.
  - The `try` and `except` block is is used to catch and handle exceptions. Where if the execution in the `try` clause run into an exception, if its type matches the exception named after the `except` keyword, `except` clause will run. If no error occurs, the `except` clause is skipped and execution of the try statement is finished.
  - If there is no exception named after the `except` keyword, the `except` clause will be executed for all exception.
  - If there is no exception occur the `else` clause will be executed.
  - Use`finally` at the last clause to execute sections of code that should always run, with or without any previously encountered exceptions.

  3. Things to notice:
  - If there's an exception happened during the execution of the `try` clause, the rest of the clause is skipped.
  - The class hierarchy for built-in exceptions is:
  ```mermaid
  - BaseException
    -  ├── BaseExceptionGroup
    -  ├── GeneratorExit
    -  ├── KeyboardInterrupt
    -  ├── SystemExit
    -  └── Exception
        - ├── ArithmeticError
        - │    ├── FloatingPointError
        - │    ├── OverflowError
        - │    └── ZeroDivisionError
        - ├── AssertionError
        - ├── AttributeError
        - ├── BufferError
        - ├── EOFError
        - ├── ExceptionGroup [BaseExceptionGroup]
        - ├── ImportError
        - │    └── ModuleNotFoundError
        - ├── LookupError
        - │    ├── IndexError
        - │    └── KeyError
        - ├── MemoryError
        - ├── NameError
        - │    └── UnboundLocalError
        - ├── OSError
        - │    ├── BlockingIOError
        - │    ├── ChildProcessError
        - │    ├── ConnectionError
        - │    │    ├── BrokenPipeError
        - │    │    ├── ConnectionAbortedError
        - │    │    ├── ConnectionRefusedError
        - │    │    └── ConnectionResetError
        - │    ├── FileExistsError
        - │    ├── FileNotFoundError
        - │    ├── InterruptedError
        - │    ├── IsADirectoryError
        - │    ├── NotADirectoryError
        - │    ├── PermissionError
        - │    ├── ProcessLookupError
        - │    └── TimeoutError
        - ├── ReferenceError
        - ├── RuntimeError
        - │    ├── NotImplementedError
        - │    └── RecursionError
        - ├── StopAsyncIteration
        - ├── StopIteration
        - ├── SyntaxError
        - │    └── IndentationError
        - │         └── TabError
        - ├── SystemError
        - ├── TypeError
        - ├── ValueError
        - │    └── UnicodeError
        - │         ├── UnicodeDecodeError
        - │         ├── UnicodeEncodeError
        - │         └── UnicodeTranslateError
        - └── Warning
                - ├── BytesWarning
                - ├── DeprecationWarning
                - ├── EncodingWarning
                - ├── FutureWarning
                - ├── ImportWarning
                - ├── PendingDeprecationWarning
                - ├── ResourceWarning
                - ├── RuntimeWarning
                - ├── SyntaxWarning
                - ├── UnicodeWarning
                - └── UserWarning