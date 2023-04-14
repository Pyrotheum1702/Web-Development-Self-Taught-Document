from abc import ABC, abstractmethod

# Abstract class example:
class Animal(ABC):
    speed = 0
    quote = ""

    # Abstract method example
    @abstractmethod
    def walk(self):
      pass

    # Abstract method example
    @abstractmethod
    def speak():
      pass


class Dog(Animal):

    def walk(self) -> None:
      print('Walking')

    def speak() -> None:
      print('GAU GAU GAU GAU GAU')
