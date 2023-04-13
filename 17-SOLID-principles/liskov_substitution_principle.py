# Liskov substitution principle

# Violate liskov substitution principle example:
class Animal:
    def walk(self) -> None:
        print('I am an Animal and i can walk')


class Human(Animal):
    def walk(self) -> None:
        print('I am a Human and i can walk')


class Snake(Animal):
    def walk(self) -> None:
        print('I am a Snake and i can not walk')


def make_animals_walk(animals: list) -> None:
    for animal in animals:
        animal.walk()

# Test section:

animal = Animal()
human = Human()
snake = Snake()

animals = [animal, human, snake]

make_animals_walk(animals)
# Result:
# I am an Animal and i can walk
# I am a Human and i can walk
# I am a Snake and i can not walk


print('-------------------')

# Following liskov substitution principle example:

class Animal:
    def walk(self) -> None:
        print('I am an Animal and i can walk')


class Human(Animal):
    def walk(self) -> None:
        print('I am a Human and i can walk')


class LimblessAnimal:
    def slither(self) -> None:
        print('I am a Limbless Animal and i can slither')

class Snake(LimblessAnimal):
    def slither(self) -> None:
        print('I am a Snake and i can slither')


def make_animals_walk(animals: list) -> None:
    for animal in animals:
        animal.walk()

def make_limbless_animal_slither(limbless_animals: list) -> None:
    for limbless_animal in limbless_animals:
        limbless_animal.slither()


# Test section:

animal = Animal()
human = Human()

animals = [animal, human]

make_animals_walk(animals)
# Result:
# I am an Animal and i can walk
# I am a Human and i can walk

limbless_animal = LimblessAnimal()
snake = Snake()

limbless_animals = [limbless_animal, snake]

make_limbless_animal_slither(limbless_animals)
# Result:
# I am a Limbless Animal and i can slither
# I am a Snake and i can slither
