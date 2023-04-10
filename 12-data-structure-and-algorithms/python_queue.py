# Implementation using list:
# Python’s built-in data structure list can be used as a queue.

class queue(list):
    def __init__(self, value_list):
        self.queue = value_list

    def __iter__(self):
        self.index = 0
        return self.queue

    def __next__(self):
        return_value = self.queue[self.index]
        self.index += 1
        return return_value

    # Return whether the queue is empty
    def is_empty(self):
        if len(self.queue) is 0:
            return True
        else:
            return False

    # Return number of element in the queue
    def get_size(self):
        return len(self.queue)

    # Return the item in front of the queue
    def get_front(self):
        return self.queue[0]

    # Return the last item of the queue
    def get_rear(self):
        return self.queue[len(self.queue)-1]
    # Push an item to the queue

    # Enqueue an item
    def enqueue(self, item):
        self.queue.append(item)

    # Dequeue the item at the front
    def dequeue(self):
        return self.queue.pop(0)

    # Print queue as a list
    def print(self):
        temp_list = []
        for i in self.queue:
            temp_list.append(i)
        print(temp_list)
    # Clear queue

    def clear(self):
        self.queue.clear()


queue = queue([])

# enqueue(x) is used to add an item into the queue
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(4)
queue.enqueue(8)
queue.enqueue(16)
queue.enqueue(32)
queue.print()
# Result: [1, 2, 4, 8, 16, 32]

# pop(0) function to pop out the earliest item that was added to the queue
print("popped item:", queue.dequeue())
queue.print()
# Result: [2, 4, 8, 16, 32]
print("popped item:", queue.dequeue())
queue.print()
# Result: [4, 8, 16, 32]

# Get the item that's in the front of the queue
print(queue.get_front())
# Result: 4

# Get the item that's in the back of the queue
print(queue.get_rear())
# Result: 32

# Get the number of item in the queue (size)
print("size of queue:", queue.get_size())

# Whether the queue is empty or not
print("is queue empty:", queue.is_empty())

# Clear queue
queue.clear()

# Whether the queue is empty or not
print("is queue empty:", queue.is_empty())
