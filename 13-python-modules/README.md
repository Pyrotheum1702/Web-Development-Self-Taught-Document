# Content Overview

# Python Module
1. Lesson content:
  What is a module
  How to import a module
2. What i learned:
  - Module:
    - A module is a file containing Python definitions and statements. The file name is the module name with the exclude .py extension. Grouping related code into a module makes the code easier to understand and use. It also makes the code logically organized.
    -
  - We can import a module to another module using the import statement.
    - Syntax: `import` + module name
  - The `from`-`import` statement:
    - Python’s from statement lets you import specific attributes from a module without importing the module as a whole.
    - Syntax: `from` + module name + `import` + attribute
  - Import all:
    - The `*` symbol used with the `from`-`import` statement is used to import everything from a module to current namespace or current module, it's like append the module to current module after the import line.
    - The use of `*` has its advantages and disadvantages. If you know exactly what you will be needing from the module, it is not recommended to use *, else do so.
  - Import a module as different name:
    - You can rename the module while importing it using the keyword `as`.
    - Syntax: `import` + module name + `as` + name
  - Built-in modules:
    - Python built-in module could be found here: https://docs.python.org/3/library/