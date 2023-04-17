# Content Overview
  1. SOLID Principles
  2. Single Responsibility Principle
  3. Open/Closed Principle
  4. Liskov Substitution
  5. Interface Segregation Principle
  6. Dependency Inversion Principle
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
      - For instance: `attack()` is a method that perform an attack in a way of given `attack_method`, if the given `attack_method` is `AttackMethod.PUNCH` it's will do punch .ect.. using switch statement for instance. So whenever we need to implement a new way of attack, we will have to modify the `attack()` method of `Human` class, essentially modifying `Human` class. This violate the Open/Closed principle, To comply with this principle we will make a new class `AttackBase` with a abstract method `attack()` so for every new way of attacking we just need to make new class inherit from `AttackBase` class and override `attack()` method, example: `AttackMethodPunch(AttackBase)`. Back in `attack()` method of `Human` class, it will now be `attack(AttackMethodBase attack_method)`, we will make it just call `attack()` from of given `attack_method`. From this, whenever we want to implement a new way of attack, we just need to create a new class and inherits from `AttackBase`(mean extending), without modifying `Human` class(mean not modifying).
# Liskov Substitution Principle
1. What i learned:
  - Liskov Substitution principle states that subclasses should be substitutable for their base classes.
    - This means that, given that class B is a subclass(child class) of class A, we should be able to pass an object of class B to any method that expects an object of class A and the method should not give any weird output in that case.
  - Example `Human` and `Snake` is a subclass(child class) of `Animal` class:
    - There is a method expect a `Animal` object as an argument and call `walk()` method of that object, a `Human` and `Snake` objects should be substitutable for that argument without getting any weird result. But in this case `Human` can walk but `Snake` does not, `Snake` do the slithering instead. This violate the principle, because `Snake` can't walk. To comply to the principle, we would make a new class `LimblessAnimal` that do `slither()` instead of `walk()` and have `Snake` class inherit from it instead. Now, `Human` is substitutable for `Animal` and `Snake` is substitutable for `LimblessAnimal`, everyone is happy now.
  - When a class does not obey this principle, it leads to some nasty bugs that are hard to detect.
# Interface Segregation Principle
1. What i learned:
  - Interface segregation means that overall it's better to have several specific interfaces as opposed to one general purpose interface.
  - Segregation means keeping things separated, and the Interface Segregation Principle is about separating the interfaces.
  - The principle states that many client-specific interfaces are better than one general-purpose interface. Clients should not be forced to implement a function they do no need.
  - A class should not be forced to depend on methods it does not use.
  - Example `Human`, `Bird`, `Snake` are subclass(child class) of `Animal` class:
    - `Animal` has methods like `walk()`, `slither()`, `fly()` which are inherited by `Human`, `Bird` and `Snake`. This is violating the principle because for instance `Human` would get `slither()` and `fly()` which it does not use, human can not fly or slither. The same for `Bird` and `Snake`. To comply to the principle, `Human` should only able to `walk()` and `Snake` do `slither()`, `Bird` do `fly()`, keep them separately.
# Dependency Inversion Principle
1. What i learned:
  - The Dependency Inversion principle states that our classes should depend upon interfaces or abstract classes instead of concrete classes and functions.
    -  Concrete class is a class that has a definition for all its methods and has no abstract method.
  - So the principle is mean to gather the use of abstract class and abstract methods over concrete classes and functions.

2. Wikipedia statement (very hard to understand):
  - High-level modules should not import anything from low-level modules. Both should depend on abstractions (e.g., interfaces).
  - Abstractions should not depend on details. Details (concrete implementations) should depend on abstractions.
