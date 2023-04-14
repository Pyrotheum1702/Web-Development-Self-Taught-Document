from abc import ABC, abstractmethod

# Dependency Inversion principle example:
# Use of abstract class


class Creature(ABC):
    pass


class Animal(Creature):

    @abstractmethod
    def walk(self) -> None:
        pass


class FlyingAnimal(Creature):

    @abstractmethod
    def fly(self) -> None:
        pass


class LimblessReptile(Creature):

    @abstractmethod
    def slither(self) -> None:
        pass


class Human(Animal):
    def walk(self) -> None:
        print('Im a Human and i walk')


class Bird(FlyingAnimal):

    def fly(self) -> None:
        print('Im a Bird and i fly')


class Snake(LimblessReptile):

    def slither(self) -> None:
        print('Im a Snake and i slither')

# Test section:

duoc = Human()
billy = Bird()
be_na = Snake()

duoc.walk()
billy.fly()
be_na.slither()
