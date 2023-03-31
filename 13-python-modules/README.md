# Content Overview
1. Python Module
2. Package Manager
3. Virtual Environment
# Python Module
1. Lesson content:
  - What is a module
  - How to import a module
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
# Package Manager
1. Lesson Content:
  - PIP
2. What i learned:
  - What is PIP:
    - PIP is a package manager for Python packages
    - You need PIP to install packages from the Python Package Index and other indexes.
    - Pip connects to an online repository of public packages, called the Python Package Index.
    - The Python Software Foundation recommends using pip for installing Python applications and its dependencies during deployment.
  - If you have Python version 3.4 or later, PIP is included by default.
  - To check pip version use: `pip --version` on terminal
  - If you do not have PIP installed, you can find it here: https://pypi.org/project/pip/
  - You can find python packages from here: https://pypi.org/
  - To install a package use this syntax:
    - `pip install` + package name
# Virtual Environment
1. Lesson Content:
  - Virtual environment
  - Conda
2. What i learned:
  - Virtual environments are isolated environments that use to keep dependencies for different projects separated.
    - For instance: project A need Django ver 4.0, project B need Django ver 4.1, we could make that possible by create 2 different virtual environment for them.
  - By default, every project on your system will share the same site packages, except for projects in virtual environments which those projects are isolated, separated and have their own packages that also not share with projects anywhere else.
  - Conda:
    - Conda is an open source package management system and environment management system that runs on Windows, macOS, and Linux. Conda easily creates, saves, loads and switches between environments on your local computer.
    - Basically Conda help you to manage packages and environments in the same software.