# Content Overview
1. Python Decorator
# Python Decorator
1. Lesson content:
  - What is decorator
  - First class object concept
2. What i learned:
  - What is decorator:
    - A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure.
    - Decorators are usually called before the definition of a function you want to decorate.
    - A Decorator could be describe as a food wrapper wrapping around a food, where food is a function.
  - In Python, functions are *first class objects* which means that functions in Python can be used or passed as arguments.
  - Properties of first class functions:
    -  A function is an instance of the Object type.
    -  You can store the function in a variable.
    -  You can pass the function as a parameter to another function.
    -  You can return the function from a function.
    -  You can store them in data structures such as hash tables, lists, ...
  - `@decorator-name`: to apply decorators to a function.
  - Chaining decorator:
    - Means decorating a function with multiple decorators.
3. Notice:
  - `fuction` vs `function()`: `function` is a function object, `function()` a function call