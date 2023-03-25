# Content Overview
1. Python Iterator
# Python Iterator
1. Lesson content:
  - What is an iterator
  - Iterator, Iterating concept
  - Iterator vs iterable
2. What i learned:
  - What is an iterator:
    - An iterator is an object that contains a countable number of value.
    - An iterator is an object that can be iterated upon, meaning that you can traverse through all the value.
    - A Python object is considered an iterator when it implements two special methods known as the *iterator protocol*. Which consist of the methods `__iter__()` and `__next__()`, must have both.
  - What is an iterable:
    - Iterable is a word to describe that an object could be loop over in a `for` loop.
  - The process of looping over the elements is iterating
  - The most generic use case of a Python iterator is to allow iteration over a stream of data or a container data structure. Python uses iterators under the hood to support every operation that requires iteration.
  - Iterators come in handy when you need to iterate over a dataset or data stream with an unknown or a huge number of items.
  - Lists, tuples, dictionaries, and sets are all iterable objects. They are *iterable containers* which you can get an iterator from.
  - `iter()`: return an iterator from an object, the argument must supply an iterator or sequences.
  - `__iter__()`: Called to initialize the iterator. It must return an iterator object, typically return the object itself.
  - `__next__()`: Called to iterate over the iterator. It must return the next value from the container.
  - Repeated call to `__next__()` will go through the collection one item at a time, When there is nothing left to iterate over, a StopIteration Exception is raised.
3. Related:
  - The `for` loop actually creates an iterator object and executes the next() method for each loop and exit when it's finished.