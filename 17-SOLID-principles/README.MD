# Content Overview
  1. SOLID Principle
  2. Single Responsibility Principle
  3. Open/Closed Principle
# SOLID Principle
# Single Responsibility Principle
1. What i learned:
  - The idea is a class should have only one reason to change.
    - Example `Human` class:
      - It's responsibility is to simulate Human race from the real world, therefore the only reason to change it, is to change how it simulate a Human.
      - For instance: It's has methods like `walk()`, `speak()`, `eat()` changing them is valid and make sense because those methods simulate how a Human would behave, match to it's responsibility of simulating Human race.
      - For instance: It's has the method `print_information()` for printing information of a human object on the terminal, this method violate the single responsibility rule because it's has a different responsibility of printing information, therefore if we want to change how it's print information we have to change `Human` class, which mean now `Human` have 2 reason to change. 1 is to change how it simulate ,2 is how it print information. Therefore it's must be moved into a different class that has a responsibly to print the information of a Human.
# Open/Closed Principle