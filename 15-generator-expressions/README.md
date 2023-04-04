# Generator Expression
1. Lesson content:
  - Generator
  - Generator Expression
2. What i learned:
  - What is generator:
    - Generator provide a convenient way to implement the iterator protocol, generator is an iterable created using a function with a yield statement.
  - Generator function:
    - The generator function contains one or more yield statements instead of a return statement.
    - Local variables and their states are remembered between successive calls.
    - Once the function yields, the function is paused and the control is transferred to the caller.
    - When the function terminates, StopIteration is raised automatically on further calls.
  - What is generator expression:
    - A generator expression is an expression that returns a generator (generator object).
  - The main feature of generator expression is evaluating the elements on demand.
  - Generator expression syntax and concept are similar to list comprehension, the different are the parentheses to square bracket and the expression result type.