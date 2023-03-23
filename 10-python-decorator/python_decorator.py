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

# tore function in a list
func_list = []
func_list.append(say_hello_world)
func_list.append(say_i_love_programming)
func_list.append(say_i_want_to_be_rich)

# Call all functions in the func_list
for func in func_list:
  print("called function:", call_function(func))

# This Decorator function print "Wrapper" before and after the decorated function call
def wrapper_1(func):
  def wrapper():
    print("Wrapper 1")
    func()
    print("Wrapper 1")
  return wrapper

def wrapper_2(func):
  def wrapper():
    print("Wrapper 2")
    func()
    print("Wrapper 2")
  return wrapper

# Normal undecorated functions:
def print_pork():
  print("Pork")
def print_chicken():
  print("Chicken")
def print_steak():
  print("Steak")


# Without decorator:
print_pork()
# Result: Pork
print_chicken()
# Result: Chicken
print_steak()
# Result: Steak

# Applying decorator:
@wrapper_1
def print_pork():
  print("Pork")
# +
@wrapper_1
def print_chicken():
  print("Chicken")
# +
@wrapper_1
def print_steak():
  print("Steak")

# With decorator:
print_pork()
# Result: Wrapper 1 /n Pork /n Wrapper 1
print_chicken()
# Result: Wrapper 1 /n Chicken /n Wrapper 1
print_steak()
# Result: Wrapper 1 /n Steak /n Wrapper 1

# Applying chain decorator:
@wrapper_2
@wrapper_1
def print_pork():
  print("Pork")
# +
@wrapper_2
@wrapper_1
def print_chicken():
  print("Chicken")
# +
@wrapper_2
@wrapper_1
def print_steak():
  print("Steak")

# With chain decorator:
print_pork()
# Result: Wrapper 2 /n Wrapper 1 /n Pork /n Wrapper 1 /n Wrapper 2
print_chicken()
# Result: Wrapper 2 /n Wrapper 1 /n Chicken /n Wrapper 1 /n Wrapper 2
print_steak()
# Result: Wrapper 2 /n Wrapper 1 /n Steak /n Wrapper 1 /n Wrapper 2