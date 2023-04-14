class Animal:
    speed = 0
    health = 0
    health_point = 0

    def walk(self):
        print('Walk at', self.speed, 'speed')

# Inheritance example:


class Human(Animal):
    name = 'Unknown'
    intelligent = 0

    def speak(self, quote: str):
        print(self.name, 'say:', quote)

# Inheritance example where Human has speed, health_point, strength (properties)
# from Animal class with the addition intelligent, name property and speak method.

# Test section:


duoc = Human()
duoc.name = 'Duoc'
duoc.speed = 9
duoc.strength = 8
duoc.intelligent = 7
duoc.health_point = 7

print(duoc.name, 'speed:', duoc.speed)
print(duoc.name, 'strength:', duoc.strength)
print(duoc.name, 'intelligent:', duoc.intelligent)
print(duoc.name, 'health_point:', duoc.health_point)
duoc.speak('With the right conditions and actions, anyone could achieve their')
# Result:
# Duoc speed: 9
# Duoc strength: 8
# Duoc intelligent: 7
# Duoc health_point: 7
