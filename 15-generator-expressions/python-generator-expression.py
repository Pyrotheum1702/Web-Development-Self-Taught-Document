# Function create generator object example:
def square_generator(iteration: int):
    for i in range(iteration):
        yield (i+1) ** 2

squares = square_generator(10)
print(type(squares))
# Result: generator object

list_1 = []

# Since generator object are iterable, we could put it in a for loop
for i in squares:
    list_1.append(i)

print(list_1)
# Result: list_1 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#---------------------------

# Generator expression example:

# Same functionality as square_generator using generator expression
iteration = 15
squares = ((i+1)**2 for i in range(iteration))
print(type(squares))
# Result: generator object

list_2 = []

for i in squares:
    list_2.append(i)

print(list_2)
# Result: list_2 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225]


# Multiple yield example:

def generate_albert_einstein_quotes():
  yield 'Life is like riding a bicycle. To keep your balance, you must keep moving.'
  yield 'I never think of the future. It comes soon enough.'
  yield 'Imagination is more importance than knowledge.'

albert_einstein_quotes = generate_albert_einstein_quotes()

for quote in albert_einstein_quotes:
  print(quote)
# Result:
# Life is like riding a bicycle. To keep your balance, you must keep moving.
# I never think of the future. It comes soon enough.
# Imagination is more importance than knowledge.

# explanation: since once the function yields, the function is paused, when the function is called again, it's will start executing where it left off.

albert_einstein_quotes = generate_albert_einstein_quotes()

print(next(albert_einstein_quotes))
print(next(albert_einstein_quotes))
print(next(albert_einstein_quotes))
# Result:
# Life is like riding a bicycle. To keep your balance, you must keep moving.
# I never think of the future. It comes soon enough.
# Imagination is more importance than knowledge.