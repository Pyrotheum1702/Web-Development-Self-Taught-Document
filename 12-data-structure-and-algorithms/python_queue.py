# Implementation using list:
# Python’s built-in data structure list can be used as a queue.

queue = []

# append(x) is used to add an item into the queue
queue.append(1)
queue.append(2)
queue.append(4)
queue.append(8)
queue.append(16)
queue.append(32)
print(queue)
# Result: [1, 2, 4, 8, 16, 32]

# pop(0) function to pop out the earliest item that was added to the queue
print("popped item:", queue.pop(0))
print(queue)
# Result: [2, 4, 8, 16, 32]
print("popped item:", queue.pop(0))
print(queue)
# Result: [4, 8, 16, 32]

# Get the item that's in the front of the queue
print(queue[0])
# Result: 4

# Get the item that's in the back of the queue
print(queue[-1])
# Result: 32

# Get the number of item in the queue (size)
print("size of queue:", len(queue))

# Whether the queue is empty or not
print("is queue empty:", not queue)

# Clear queue
queue.clear()

# Whether the queue is empty or not
print("is queue empty:", not queue)
