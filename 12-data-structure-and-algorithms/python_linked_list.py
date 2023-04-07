# Node of the linked list
class Node:
  def __init__(self, value: any, node = None):
    self.value = value
    self.next_node = node

  # Set the next node point to
  def set_next_node(self, node):
    self.next_node = node

  # Get the value of the node
  def get_value(self):
    return self.value

# Linked List Class
class LinkedList:
  def __init__(self, head: Node):
    self.head = head
    self.tail = None

  # append: append a new node to the tail of the list, making it the new tail node
  def append(self, value):
    if self.tail is None:
      self.tail = Node(value, None)
      self.head.set_next_node(self.tail)
    else:
      self.tail.set_next_node(Node(value, None))
      self.tail = self.tail.next_node

  # insert: insert a node after a specified node
  def insert(self, value, node: Node):
    if node is None:
      return

    if node.next_node is None:
      node.set_next_node(Node(value, None))
      self.tail = node.next_node
    else:
      node.set_next_node(Node(value, node.next_node))

  # insert: insert a node before the head node, making that node the new head node
  def insert_head(self,value):
    new_head = Node(value, self.head)
    self.head = new_head

  def delete(self, node: Node):
    # if specified node to delete is equal to head node, make the next node of head to be the new head, delete old head afterward:
    if node == self.head:
      new_head = self.head.next_node
      self.head.next_node = None
      self.head = new_head
      return

    # this is use to traverse through the list
    temp_node = self.head

    # if specified node to delete is tail node, make the second last node to be the new tail and delete old tail:
    if node == self.tail:
      # traverse to the second last node
      while temp_node.next_node.next_node is not None:
        temp_node = temp_node.next_node
      second_last_node = temp_node
      # making the second last node point to None and second last node being the new tail where the last tail is now an orphaned and will get automatically deleted.
      self.tail = second_last_node
      second_last_node.next_node = None
      return

    # specified node to delete is in the middle of the linked list.
    # link the before and after node the specified node together and delete the specified node afterward
    while temp_node.next_node is not node:
        temp_node = temp_node.next_node
    before_node = temp_node
    before_node.next_node = node.next_node
    node.next_node = None

  # this function return the linked list as a list
  def get_list(self):
    return_value = [self.head.value]
    temp_node = self.head
    while temp_node.next_node is not None:
      return_value.append(temp_node.next_node.value)
      temp_node = temp_node.next_node
    return return_value

# Linked List test section:

linked_list_1 = LinkedList(Node(0))

inspect_node = None

linked_list_1.append(2)
linked_list_1.append(5)
linked_list_1.append(10)
linked_list_1.append(14)

# print link_list_1 as a list
print(linked_list_1.get_list())
# Result: [0, 2, 5, 10, 14]

# inspecting linked_list
inspect_node: Node = linked_list_1.head

print(inspect_node.get_value())
# Result: 0
# next item:
inspect_node = inspect_node.next_node
print(inspect_node.get_value())
# Result: 2
# next item:
inspect_node = inspect_node.next_node
print(inspect_node.get_value())
# Result: 5

# insert a node at inspec_node position
linked_list_1.insert(8, inspect_node)
print(linked_list_1.get_list())
# Result: [0, 2, 5, 8, 10, 14]

linked_list_1.insert(7, inspect_node)
print(linked_list_1.get_list())
# Result: [0, 2, 5, 8, 10, 14]

# insert a node at the tail of linked_list_1
linked_list_1.insert(15, linked_list_1.tail)
print(linked_list_1.get_list())
# Result: [0, 2, 5, 7, 8, 10, 14, 15]
linked_list_1.insert(17, linked_list_1.tail)
print(linked_list_1.get_list())
# Result: [0, 2, 5, 7, 8, 10, 14, 15, 17]

# insert a node at the head of linked_list_1
linked_list_1.insert_head(-1)
print(linked_list_1.get_list())
# Result: [-1, 0, 2, 5, 7, 8, 10, 14, 15]
linked_list_1.insert_head(-3)
print(linked_list_1.get_list())
# Result: [-3, -1, 0, 2, 5, 7, 8, 10, 14, 15]

# Delete a node from the inspect_node position
# inspect_node position recap
print(inspect_node.get_value())
linked_list_1.delete(inspect_node)
print(linked_list_1.get_list())
# Result: [-3, -1, 0, 2, 7, 8, 10, 14, 15, 17]

# Delete a node from the tail
linked_list_1.delete(linked_list_1.tail)
print(linked_list_1.get_list())
# Result: [-3, -1, 0, 2, 7, 8, 10, 14, 15]
linked_list_1.delete(linked_list_1.tail)
print(linked_list_1.get_list())
# Result: [-3, -1, 0, 2, 7, 8, 10, 14]

# Delete a node from the head
linked_list_1.delete(linked_list_1.head)
print(linked_list_1.get_list())
# Result: [-1, 0, 2, 7, 8, 10, 14]
linked_list_1.delete(linked_list_1.head)
print(linked_list_1.get_list())
# Result: [0, 2, 7, 8, 10, 14]