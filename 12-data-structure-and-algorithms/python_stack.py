# Implementation using list:
# Python’s built-in data structure list can be used as a stack.

class Stack(list):
    def __init__(self, value_list):
        self.stack = value_list

    def __iter__(self):
        self.index = 0
        return self.stack

    def __next__(self):
        return_value = self.stack[self.index]
        self.index += 1
        return return_value

    # Return whether the stack is empty
    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    # Return number of element in the stack
    def get_size(self):
        return len(self.stack)

    # Return topmost item of the stack
    def get_top(self):
        return self.stack[len(self.stack)-1]

    # Push an item to the stack
    def push(self, item):
        self.stack.append(item)

    # Pop the item at the top of the stack
    def pop(self):
        return self.stack.pop()

    # Print stack as a list
    def print(self):
        temp_list = []
        for i in self.stack:
            temp_list.append(i)
        print(temp_list)

    # Clear stack
    def clear(self):
        self.stack.clear()

stack = Stack([])

# push(x) is used to add elements to the top of the stack
stack.push(1)
stack.push(2)
stack.push(4)
stack.push(8)
stack.push(16)
stack.push(32)
stack.print()
# Result: [1, 2, 4, 8, 16, 32]

# pop() function to pop out the most recent item that was added to the stack
print("popped item:", stack.pop())
stack.print()
# Result: [1, 2, 4, 8, 16]
print("popped item:", stack.pop())
stack.print()
# Result: [1, 2, 4, 8]

# Get the upmost item on the stack
print('item at the top:', stack.top())
# Result: 8

# Get the number of item in the stack (size)
print("size of stack:", stack.size())

# Whether the stack is empty or not
print("is stack empty:", stack.empty())

# Clear stack
stack.clear()

# Whether the stack is empty or not
print("is stack empty:", stack.empty())
