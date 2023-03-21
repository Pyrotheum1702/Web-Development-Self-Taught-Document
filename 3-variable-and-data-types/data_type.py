# Integer variable declare
number = 10
print(number)
# Result: number = 10

# Float variable declare
number = 10.5058934
print(number)
# Result: number = 10.5058934

# Integer range test declare
number = 12389734859734895789347598374895729834878974356834596873495876098239032498034598346598365972309473964598709217093414759837489572983487897435683459687349587609823903249803459834659836597230947396459870921709
print(number)
# Result: integer has no limit

# Negative number declare
number = -99.4555230
print(number)
# Result: number = -99.4555230

# String variable declare
text = "i am a string"
print(text)
# Result: text = "i am a string"

# String format methods
today_is = "Friday"
day_in_week = "Today is {0} in the Week"
print(day_in_week.format(today_is))
# Result: Today is Friday in the Week
x = "my name is {}".format("Duoc")
print(x)
# Result: my name is Duoc
x = "my sister is {name}".format(name="Dung")
print(x)
# Result: my sister is Dung
x = f"my age is {10 + 11}"
print(x)
# Result: my age is 21

# complex variable declare
x = 5 + 4j
print(x)
print(type(x))
# Result: x = (5+4j)
# Result: x = <class 'list'>

# list variable declare
x = ["apple", "banana", "cherry"]
print(x)
print(type(x))
# Result: x = ["apple", "banana", "cherry"]
# Result: x = <class 'list'>

# tuple variable declare
x = ("apple", "banana", "cherry")
print(x)
print(type(x))
# Result: x = ("apple", "banana", "cherry")
# Result: x = <class 'tuple'>

# range variable declare
x = range(6)
print(x)
print(type(x))
# Result: x = range(0, 6)
# Result: x = <class 'range'>

# dict variable declare
x = {"name" : "Duoc", "age" : 21}
print(x)
print(type(x))
# Result: x = {"name" : "Duoc", "age" : 21}
# Result: x = <class 'dict'>

# set variable declare
x = {1,2,2,3,3,4,1,4,5}
print(x)
print(type(x))
# Result: x = {1, 2, 3, 4, 5}
# Result: x = <class 'set'>

# set variable declare
x = frozenset({1,2,2,3,3,4,1,4,5})
print(x)
print(type(x))
# Result: x = {1, 2, 3, 4, 5}
# Result: x = <class 'frozenset'>

# boolean variable declare
x = False
print(x)
print(type(x))
# Result: x = False
# Result: x = <class 'bool'>

# bytes variable declare
x = b"Hello"
print(x)
print(type(x))
# Result: x = b'Hello'
# Result: x = <class 'bytes'>

# bytearray variable declare
x = bytearray(12)
print(x)
print(type(x))
# Result: x = bytearray(b'\x00\x00\x00\x00\x00')
# Result: x = <class 'bytearray'>

# memoryview variable declare
x = memoryview(bytes(8))
print(x)
print(type(x))
# Result: x = <memory at 0x00000296FBF047C0>
# Result: x = <class 'memoryview'>

# None variable declare
x = None
print(x)
print(type(x))
# Result: x = None
# Result: x = <class 'NoneType'>
