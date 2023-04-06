
class Test:
    # __init__() one of the magic method.
    def __init__(self):
        print('i was printed in __init__() method!')

# __init__() is called on object creation.
test_1 = Test()
# Result: i was printed in __init__() method!

# __init__() again.
test_2 = Test()
# Result: i was printed in __init__() method!

# use dir() to get magic methods of a class printed
print(dir(Test))
# Result:
#  '__class__',
#  '__delattr__',
#  '__dict__',
#  '__dir__',
#  '__doc__',
#  '__eq__',
#  '__format__',
#  '__ge__',
#  '__getattribute__',
#  '__getstate__',
#  '__gt__',
#  '__hash__',
#  '__init__',
#  '__init_subclass__',
#  '__le__',
#  '__lt__',
#  '__module__',
#  '__ne__',
#  '__new__',
#  '__reduce__',
#  '__reduce_ex__',
#  '__repr__',
#  '__setattr__',
#  '__sizeof__',
#  '__str__',
#  '__subclasshook__',
#  '__weakref__'