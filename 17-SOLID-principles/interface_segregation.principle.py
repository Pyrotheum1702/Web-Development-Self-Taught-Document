
# Violate Interface Segregation principle:
class Animal():

    def slither(self) -> None:
        pass

    def walk(self) -> None:
        pass

    def fly(self) -> None:
        pass


class Human(Animal):

    def walk(self) -> None:
        print('Im a Human and i walk')


class Bird(Animal):

    def fly(self) -> None:
        print('Im a Bird and i fly')


class Snake(Animal):

    def slither(self) -> None:
        print('Im a Snake and i slither')

# Test section:


duoc = Human()
billy = Bird()
be_na = Snake()

duoc.walk()
billy.fly()
be_na.slither()

# Unused methods
duoc.fly()
duoc.slither()
# +
billy.walk()
billy.slither()
# +
be_na.fly()
be_na.walk()


print('--------------------')

# Following Interface Segregation principle:

class Creature:
    pass


class Animal(Creature):
    pass


class FlyingAnimal(Creature):
    pass


class LimblessReptile(Creature):
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

# Unused methods
# None.
