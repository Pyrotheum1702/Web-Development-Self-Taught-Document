# Violate single responsibility principle example:
class Human:
    def __init__(self) -> None:
        self.__speed = 0
        self.__health = 0
        self.__intelligent = 0

    def get_speed(self) -> int:
        return self.__speed

    def get_health(self) -> int:
        return self.__health

    def get_intelligent(self) -> int:
        return self.__intelligent

    def eat() -> None:
        pass

    def walk() -> None:
        pass

    def speak() -> None:
        pass

    def print_information(self) -> None:
        print('Speed:', self.__speed)
        print('Health:', self.__health)
        print('Intelligent:', self.__intelligent)


# Following single responsibility principle example:
class Human:
    def __init__(self) -> None:
        self.__speed = 0
        self.__health = 0
        self.__intelligent = 0

    def get_speed(self) -> int:
        return self.__speed

    def get_health(self) -> int:
        return self.__health

    def get_intelligent(self) -> int:
        return self.__intelligent

    def eat() -> None:
        pass

    def walk() -> None:
        pass

    def speak() -> None:
        pass


class HumanInformationPrinter:
    @staticmethod
    def print_information(human: Human) -> None:
        print('Speed:', human.get_speed())
        print('Health:', human.get_health())
        print('Intelligent:', human.get_intelligent())


# Test section

duoc = Human()

HumanInformationPrinter.print_information(duoc)
