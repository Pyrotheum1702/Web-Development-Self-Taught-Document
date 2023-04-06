# Content Overview
1. Python Object Oriented Programming
2. Inheritance
3. Encapsulation
4. Abstraction
5. Polymorphism
6. Python Magic Methods
# Python Object Oriented Programming
1. Lesson Content:
  - Object oriented programming (OOP)
  - Classes
  - Objects
2. What i learned:
  - What is OOP:
    -  The idea behind OOP is the concept of relying on classes and object.
    -  Are designed for flexible code re-use.
    - Most important concept:
      - Class.
      - Object.
      - Inheritance.
      - Encapsulation.
      - Abstraction.
      - Polymorphism.
    - Can be made more robust with features like:
      - Abstract classes.
      - Virtual functions.
      - Interfaces.
      - Multiple inheritance.
  - What are classes:
    - Classes provide a means of bundling data and functionality together.
    - Classes can be understand as a blueprint to instantiate objects.
    - Creating a new class creates a new type of object.
  - What are objects:
    - Objects are instances that are created from a class. Objects has their own data members and functionality, often called attributes that were given by the class instantiate them.
    - The word Object and Instance refer to the same thing.
# Inheritance
1. What i learned:
  - Inheritance is a concept of a class inherits or derive all the methods and properties from another class.
    - Where the parent class is the class being inherited from, also called base class.
    - And Child class is the class that inherits from the parent class, also called derived class.
# Encapsulation
1. What i learned:
  - Encapsulation is a concept of restricting the access to methods and variables directly to prevent the accidental modification of data.
  - In encapsulation, the variables of a class will be hidden from other classes, and can be accessed only through the methods of their current class.
  - While coding we don't have a way to restrict the access of member function and data so we use a naming to convention to pretend that's they are not accessible by other class.
    - `var`: public, accessible globally
    - `_var`: protected, accessible but it's class and subclasses.
    - `__var`: private, accessible only within it's own class.
  - But in runtime, Python actually does support for private variables through a double underscore `(i.e. __name)`. It will actually raise an error!
# Abstraction
1. What i learned:
  - Abstraction is defined as a process of handling complexity by hiding unnecessary information from the user.
  - That enables the user to implement even more complex logic on top of the provided abstraction without understanding or even thinking about all the hidden background/back-end complexity.
  - Abstraction allow you to just know how to use it without needing to understand how it work.
# Polymorphism
1. What i learned:
  - Polymorphism is the concept of an object having many forms. In Programming in particular inherited methods could be overripen to achieve different behavior to the version from the base class, then when multiple child class having the same method from a parent class but with different behavior, that's method is having multiple form. That's Polymorphism.
# Python Magic Methods
1. Lesson Content:
  - Magic methods
2. What i learned:
  - What is magic methods:
    - Magic methods are the special methods that start and end with the double underscores.
    - Also called dunder method
  - Magic methods are not meant to be invoked directly by you, but the invocation happens internally from the class on a certain action.
    - Example: `__init__()` will be called when an object is created.
  - Built-in classes in Python define many magic methods. Use the `dir()` function to see the number of magic methods inherited by a class.