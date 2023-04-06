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
        print('name:', self.__name)
        print('speed:', self.__speed)
        print('strength:', self.__strength)
        print('intelligent:', self.__intelligent)
        print('health_point:', self.__health_point)


duoc = Human()
duoc.set_name('Duoc')
duoc.set_speed(9)
duoc.set_strength(8)
duoc.set_intelligent(7)
duoc.set_heath_point(7)

# Abstraction is defined as a process of handling complexity,
# by hiding unnecessary information from the user.

# So you could understand as the method print_information()
# will print all the information of the object. You dont need
# to know how it do it, you just need to know how to use it and what it does.
duoc.print_information()
# Result :
# name: Duoc
# speed: 9
# strength: 8
# intelligent: 7
# health_point: 7
