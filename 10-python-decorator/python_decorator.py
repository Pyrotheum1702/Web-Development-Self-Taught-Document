def say_hello_world():
  print('Hello World!')

def say_i_love_programming():
  print('I Love Programming!')

def say_i_want_to_be_rich():
  print('I Want to be Rich!')

# this function call a function and return it
def call_function(func):
  func()
  called_func = func
# you can return a function
  return called_func

# function as argument example:
call_function(say_hello_world)
# Result: Hello_World!

# Store function in a list
func_list = []
func_list.append(say_hello_world)
func_list.append(say_i_love_programming)
func_list.append(say_i_want_to_be_rich)

# Call all functions in the func_list
for func in func_list:
  print("called function:", call_function(func))

# This Decorator function print "Wrapper" before and after the decorated function call
def ability_to_move(func):
  def wrapper():
    func()
    print("Moveable")
  return wrapper

def ability_to_speak(func):
  def wrapper():
    func()
    print("Speakable")
  return wrapper

# Normal undecorated functions:
def print_human():
  print("Human")
def print_cow():
  print("Cow")
def print_lion():
  print("Lion")


# Without decorator:
print_human()
# Result: Pork
print_cow()
# Result: Chicken
print_lion()
# Result: Steak

# With decorator:
@ability_to_move
def print_cow():
  print("Cow")
@ability_to_move
def print_lion():
  print("Lion")
# Chaining decorator:
@ability_to_speak
@ability_to_move
def print_human():
  print("Human")
# Where Human and animal share the same ability to move, but. Human can speak and animal can not
# So `print_human` has both `ability_to_move` and `ability_to_speak`

# Decorated function result:
print_cow()
# Result: Cow \n Moveable
print_lion()
# Result: Lion \n Moveable
print_human()
# Result: Human \n Moveable \n Speakable
