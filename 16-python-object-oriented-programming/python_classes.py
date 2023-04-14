# Classes and objects example:

# Classes example:
class Human:
    def __init__(self):
        self.name = 'Unknown'
        self.speed = 0
        self.strength = 0
        self.intelligent = 0
        self.health_point = 0

    def print_information(self):
        print(self.name, 'speed:', self.speed)
        print(self.name, 'strength:', self.strength)
        print(self.name, 'intelligent:', self.intelligent)
        print(self.name, 'health_point:', self.health_point)

# classes can be use as blueprint to print out objects that has attributes from that class


# Objects example, where we instantiate 2 Human object. They have the same attributes but their data members are separated:
duoc = Human()
thanh = Human()

# duoc has it own name, speed, strength, intelligent, heath_point..
duoc.name = 'Duoc'
duoc.speed = 9
duoc.strength = 8
duoc.intelligent = 7
duoc.health_point = 7

# thanh has it own name, speed, strength, intelligent, heath_point..
thanh.name = 'Thanh'
thanh.speed = 4
thanh.strength = 4
thanh.intelligent = 8
thanh.health_point = 9

# so both duoc and thanh has their own data members, but same attributes because they were created from a same class

duoc.print_information()
# Result :
# Duoc speed: 9
# Duoc strength: 8
# Duoc intelligent: 7
# Duoc health_point: 7

thanh.print_information()
# Result :
# Thanh speed: 4
# Thanh strength: 4
# Thanh intelligent: 8
# Thanh health_point: 9
