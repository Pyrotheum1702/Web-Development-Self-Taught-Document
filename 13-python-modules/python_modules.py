# Import module example:
import hello_world

# Test module:
hello_world.print_hello_world()
# Result: Hello World!

# If you intend to use a function often you can assign it to a local name:
hello_world = hello_world.print_hello_world

hello_world()
# Result: Hello World!

# from-import statement test:

# As stated,the from-import statement only import the specified attribute from a module
# the color.py file has 3 function, so if i only import 1 function using the from-import statement, the other 2 should be un-imported and not accessible.
from color import print_color_red

print_color_red()
# Result: Red

print_color_blue()
# Result: not defined.
print_color_green()
# Result: not defined.

# Import all
from color import *

print_color_red()
# Result: Red
print_color_blue()
# Result: Blue
print_color_green()
# Result: Green

# Import as different name example:
import secret_of_the_universe as secret

secret.print_secret_of_the_universe()


