# Content Overview
  1. SOLID Principles
  2. Single Responsibility Principle
  3. Open/Closed Principle
# SOLID Principles
1. What i learned:
  - SOLID is intended to make designs easier to understand, maintain, and extend. Ultimately, using these design principles makes it easier for coder to avoid issues and to build adaptive, effective, and agile software.
  - SOLID with each letter stands for:
    - S: Single responsibility principle.
    - O: Open–closed principle.
    - L: Liskov substitution principle.
    - I: Interface segregation principle.
    - D: Dependency inversion principle.
# Single Responsibility Principle
1. What i learned:
  - The idea is a class should have only one reason to change.
    - Example `Human` class:
      - It's responsibility is to simulate Human race from the real world, therefore the only reason to change it, is to change how it simulate a Human.
      - For instance: It's has methods like `walk()`, `speak()`, `eat()` changing them is valid and make sense because those methods simulate how a Human would behave, match to it's responsibility of simulating Human race.
      - For instance: It's has the method `print_information()` for printing information of a human object on the terminal, this method violate the single responsibility rule because it's has a different responsibility of printing information, therefore if we want to change how it's print information we have to change `Human` class, which mean now `Human` have 2 reason to change. 1 is to change how it simulate ,2 is how it print information. Therefore it's must be moved into a different class that has a responsibly to print the information of a Human.
# Open/Closed Principle
1. What i learned:
  - Open/Closed Principle is the principle of you should be extend a class behavior without modifying it.
  - Following this principle is essential for writing code that is easy to maintain and revise.
  - Your class complies with this principle if it is:
    - Open for extension, meaning that the class’s behavior can be extended.
    - Closed for modification, meaning that the code is set and cannot be changed.
  - Example:
    - Example `Human` class with `attack(AttackMethod attack_method)` method:
      - For instance: `attack()` is a method that perform an attack in a way of given `attack_method`, if the given `attack_method` is `AttackMethod.PUNCH` it's will do punch .ect.. using switch statement for instance. So whenever we need to implement a new way of attack, we will have to modify the `attack()` method of `Human` class, essentially modifying `Human` class. This violate the Open/Closed principle, To comply with this principle we will make a new class `AttackBase` with a abstract method `attack()` so for every new way of attacking we just need to make new class inherit from `AttackBase` and override `attack()`, example: `AttackMethodPunch(AttackBase)`. Back in `attack()` method of the `Human` class, it will now be `attack(AttackMethodBase attack_method)` we will make it just call `attack()` from of given `attack_method`. From this, whenever we want to implement a new way of attack, we just need to create a new class and inherits from `AttackBase`(mean extending), without modifying `Human` class(mean not modifying).