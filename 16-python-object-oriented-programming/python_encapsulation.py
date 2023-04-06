# Encapsulation example:
class Human:
    def __init__(self):
        self.__name = 'Unknown'
        self.__speed = 0
        self.__strength = 0
        self.__intelligent = 0
        self.__health_point = 0

    def set_name(self, name: str):
        self.__name = name

    def set_speed(self, value: int):
        self.__speed = value

    def set_strength(self, value: int):
        self.__strength = value

    def set_intelligent(self, value: int):
        self.__intelligent = value

    def set_heath_point(self, value: int):
        self.__health_point = value

    def get_name(self):
        return self.__name

    def get_speed(self):
        return self.__speed

    def get_strength(self):
        return self.__strength

    def get_intelligent(self):
        return self.__intelligent

    def get_heath_point(self):
        return self.__health_point

    def print_information(self):
        print(self.__name, 'speed:', self.__speed)
        print(self.__name, 'strength:', self.__strength)
        print(self.__name, 'intelligent:', self.__intelligent)
        print(self.__name, 'health_point:', self.__health_point)


# we should'nt access the member variable directly so we use methods to do that instead.
duoc = Human()
duoc.set_name('Duoc')
duoc.set_speed(9)
duoc.set_strength(8)
duoc.set_intelligent(7)
duoc.set_heath_point(7)

# You will get AttributeError if you try to access a private member of an object
try:
    print('Name:', duoc.__name)
except AttributeError as error_message:
    print(error_message)
# Result: 'Human' object has no attribute '__name'

duoc.print_information()
# Result :
# Duoc speed: 9
# Duoc strength: 8
# Duoc intelligent: 7
# Duoc health_point: 7
