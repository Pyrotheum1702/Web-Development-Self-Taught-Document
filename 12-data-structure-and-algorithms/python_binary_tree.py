from enum import Enum, auto

class TraverseMethod(Enum):
    IN_ORDER: int = 1
    PRE_ORDER: int = 2
    POST_ORDER: int = 3
class Node:
    def __init__(self, value: int):
        self.left = None
        self.right = None
        self.value = value


class Tree:
    def __init__(self, root_node: Node):
        self.root = root_node

    # Insert a Node into the tree
    def insert(self, node: Node):
        inspect_node = self.root
        while True:
            if node.value < inspect_node.value:
                if inspect_node.left is None:
                    inspect_node.left = node
                    break
                else:
                    inspect_node = inspect_node.left
            elif node.value > inspect_node.value:
                if inspect_node.right is None:
                    inspect_node.right = node
                    break
                else:
                    inspect_node = inspect_node.right
            else:
                break

    # Return root node
    def get_root(self):
        return self.root

    # Search for if a value exist in the tree
    def search(self, value, root: Node):
        if value == root.value:
            return True

        if root.left is not None:
            if self.search(value, root.left):
                return True

        if root.right is not None:
            if self.search(value, root.right):
                return True

        return False

    # Print tree as a list
    def print_tree(self, inspect_node: Node):
        if inspect_node:
            print(inspect_node.value)

            if inspect_node.left is not None:
                self.print_tree(inspect_node.left)

            if inspect_node.right is not None:
                self.print_tree(inspect_node.right)

    def traverse(self, root: Node, traverse_method: TraverseMethod):
        return_value = []

        if root is None:
          return return_value

        match traverse_method:
          # left -> root -> right order
          case TraverseMethod.IN_ORDER:
              return_value = self.traverse(root.left, TraverseMethod.IN_ORDER)
              return_value.append(root.value)
              return_value = return_value + self.traverse(root.right, TraverseMethod.IN_ORDER)
          # root -> left -> right order
          case TraverseMethod.PRE_ORDER:
                return_value.append(root.value)
                return_value = return_value + self.traverse(root.left, TraverseMethod.PRE_ORDER)
                return_value = return_value + self.traverse(root.right, TraverseMethod.PRE_ORDER)
                return return_value
          # left -> right -> root order
          case TraverseMethod.POST_ORDER:
                return_value = self.traverse(root.left, TraverseMethod.POST_ORDER)
                return_value = return_value + self.traverse(root.right, TraverseMethod.POST_ORDER)
                return_value.append(root.value)
          case _:
              raise AssertionError('Weird traverse method')
        return return_value


list_1 = [1, 5, 2, 4, 8, 9, 0, 5, 3, 8, 10, 6, 14, 11, 17, 13]
tree = Tree(Node(7))

# Insert all items in list_1 to `tree`
for i in list_1:
    tree.insert(Node(i))


# Visit each node of `tree` in `in_order` -> [left -> root -> right] format
print(tree.traverse(tree.root_node(), TraverseMethod.IN_ORDER))
# Visit each node of `tree` in `pre_order` -> [root -> left -> right] format
print(tree.traverse(tree.root_node(), TraverseMethod.PRE_ORDER))
# Visit each node of `tree`s in `post_order` [left -> right -> root] format
print(tree.traverse(tree.root_node(), TraverseMethod.POST_ORDER))

# Print all nodes in `tree`
tree.print_tree(tree.root_node())

# search for if a value exist in the tree
print(tree.search(5, tree.root_node()))
# Result: 5 is True

# search for if a value exist in the tree
print(tree.search(500, tree.root_node()))
# Result: 500 is False
