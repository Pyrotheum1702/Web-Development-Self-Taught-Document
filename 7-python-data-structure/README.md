# Content Overview
  1. Data Structure
  2. Python Built-In Data Structure
# Data Structure
  1. Lesson content:
    - What is Data Structure in programming
  2. What i learned:
    - What is Data Structure in programming:
      - A data structure is a way of organizing data in computer memory, implemented in a programming language.
      - A data structure purpose is for efficient storage, retrieval, and modification of data.
# Python Built-In Data Structure
  1. Lesson content:
  - Built-in data structures in Python
  1. what i learned:
  - Built-in data structures in Python can be divided into two categories:
    - Mutable:
      - Definition: mutable data structures are those we can modify, adding, removing, or changing their elements.
      - Mutable data structure list:
        - list
        - set
        - dictionary
    - Immutable:
      - Definition: immutable data structures are those we can not modify or change after their creation.
      - Immutable data structure list:
        - tuple
  - List Data Structure:
    - List in Python is a dynamic mutable array which hold an ordered collection of items.
    - How to create a list
    - In Python, list can contain heterogeneous data types and objects
      - Example: integer, string, float can be stored within the same list at the same time.
    - Different elements of a list can be accessed by by an index start by 0
      - If the given index is 0 or a positive number, it will return the value from the first index forward
      - If the given index is a negative number, it will return the value from the last index backward
      - If the given index is higher than the size of the list, either positive number or negative number. An IndexError will occur.
    - Strengths of list:
      - They represent the easiest way to store a collection of related objects.
      - They are easy to modify by removing, adding, and changing elements.
      - They are useful for creating nested data structures, such as a list of lists or dictionaries.
    - Weaknesses of list:
      - They can be pretty slow when performing arithmetic operations on their elements.
      - They use more disk space because of their under-the-hood implementation.
    - List built-in methods:
      - `list.append(x)`
        - Add an item `x` to the end of the list.
      - `list.extend(iterable)`
        - Extend the list by appending all the items from the iterable
      - `list.insert(i, x)`
        - Insert an item `x` at `i` index of the element
      - `list.remove(x)`
        - Remove the first element in the list that has the value equal to `x`. Raises a ValueError if there is no such item.
      - `list.pop()`
        - Remove the item at the last element of the list and return it.
      - `list.pop(i)`
        - Remove the item at `x` index and return it.
      - `list.clear()`
        - Remove all items from the list.
      - `list.index(x)`
        - Return index of the first item has the value equal to `x`. Raises a ValueError if there is no such item.
      - `list.index(x , i)`
        - Return index of the first item has the value equal to `x`. But the search for `x` start at index `i` . Raises a ValueError if there is no such item.
      - `list.index(x , i, j)` - Return index of the first item has the value equal to `x`. But the search for `x` start at index `i` and end at `j`. Raises a ValueError if there is no such item.
      - `list.count(x)`
        - Return number of times `x` appears in the list.
      - `list.sort()`
        - Sort the items in the list.
      - `list.reverse()`
        - Reverse the order of elements of the list.
      - `list.copy()`
        - Return a copy of the list as a new object.
  - Set Data Structure:
    - A set is an unordered collection that only contain unique elements, so no duplicates are allowed.
    - How to create a set
  - Dictionary Data Structure:
    - A dictionary is an unordered collection of *keys* and *values* associated with them.
    - Dictionaries are used to quickly access certain data associated with a unique key.
    - How to create a dictionary
  - Tuple Data Structure:
    - A Tuple is an ordered collection and is immutable, mean once created, cannot be modified anymore.
    - If you try to change the value of a tuple a TypeError Exception will occur.
    - How to create a tuple