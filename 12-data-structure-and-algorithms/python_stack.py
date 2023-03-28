# Implementation using list:
# Python’s built-in data structure list can be used as a stack.

stack = []

# Instead of push(x), append(x) is used to add elements to the top of the stack
stack.append(1)
stack.append(2)
stack.append(4)
stack.append(8)
stack.append(16)
stack.append(32)
print(stack)
# Result: [1, 2, 4, 8, 16, 32]

# pop() function to pop out the most recent item that was added to the stack
print("popped item:", stack.pop())
print(stack)
# Result: [1, 2, 4, 8, 16]
print("popped item:", stack.pop())
print(stack)
# Result: [1, 2, 4, 8]

# Get the upmost item on the stack
print(stack[-1])
# Result: 8

# Get the number of item in the stack (size)
print("size of stack:", len(stack))

# Whether the stack is empty or not
print("is stack empty:", not stack)

# Clear stack then
stack.clear()

# Whether the stack is empty or not
print("is stack empty:", not stack)