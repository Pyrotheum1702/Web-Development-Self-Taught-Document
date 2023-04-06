# List Comprehensions
1. Lesson Content:
  - List Comprehension
2. What i learned:
  - What is list comprehension:
    - Is a method/a way to create a new list with less syntax or a single line of code, concise.
  - Structure:
    - Expression for item in iterable:
      - `list = [expression + iterable]`
        - Each iteration execute expression.
        - Example: `i * 2 for i in range(10)`
          - Result: list = 0 2 4 6 8 10 12 14 16 18
    - Expression for item in iterable with condition:
      - `list = [expression + iterable + condition]`
        - Each iteration execute statement if the condition is met.
        - Example: `i * 2 for i in range(10) if i % 2 == 0`
          - Result: list = 0 4 8 16
    - Expression if/else for item in iterable
      - `list = [expression_1 + condition + else + expression_2 + iterable]`
        - Each iteration execute expression but the expression outcome is depend on if/else statement.
        - Example: `'odd' if i % 2 == 1 else 'even' for i in range(10)`
          - Result: list = 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd'