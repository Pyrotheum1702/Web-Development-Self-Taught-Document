class Animal:
    _speed = 0
    _name = 'Unknown'
    _identity = 'Animal'

    def __init__(self, name = 'Unknown', speed = 0):
      self._name = name
      self._speed = speed

    def print_run_speed_with_speech(self):
        print('hi! my name is', self._name, 'and my identity is',
              self._identity, 'and i run at', self._speed, 'mph')


class Dog(Animal):
    _identity = 'Dog'

    def print_run_speed_with_speech(self):
        print('hi! my name is', self._name, 'and my identity is',
              self._identity, 'and i run at', self._speed * 1.2, 'mph')

class Cheetah(Animal):
    _identity = 'Cheetah'

    def print_run_speed_with_speech(self):
        print('hi! my name is', self._name, 'and my identity is',
              self._identity, 'and i run at', self._speed * 1.5, 'mph')

class Human(Animal):
    _identity = 'Human'

    def print_run_speed_with_speech(self):
        print('hi! my name is', self._name, 'and my identity is',
              self._identity, 'and i run at', self._speed * 0.9, 'mph')


# Polymorphism example where both Dog and Human and Cheetah classes
# were inherited from animal class and they all have the
# print_run_speed_with_speech() method. Just a little different from each other.
# where Dog get 20% bonus run speed, Cheetah get 50% run speed
# and Human get -10% run speed different to Animal class

billy = Dog('Billy', 10)
spike = Cheetah('Spike', 10)
thanh = Human('Thanh', 10)

animals = []
animals.append(billy)
animals.append(spike)
animals.append(thanh)

# In this example three competitor having the same base speed of 10 but
# because of the racial bonuses, the print_run_speed_with_speech() methods
# give different result.
for animal in animals:
  animal.print_run_speed_with_speech()
# Result:
# Dog: hi! my name is Billy and my identity is Dog and i run at 12.0 mph

# Cheetah: hi! my name is Spike and my identity is Cheetah and i run at 15.0 mph

# Human: hi! my name is Thanh and my identity is Human and i run at 9.0 mph





