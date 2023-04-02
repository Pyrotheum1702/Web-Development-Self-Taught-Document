class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class Tree:
    def __init__(self, root_node: Node):
        self.root = root_node

    # Insert a Node into the tree
    def insert(self, node: Node):
        if node:
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
    def root_node(self):
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

    # This function return the tree as a list with a left -> root -> right order
    def in_order_traversal(self, root: Node):
        return_value = []
        if root is not None:
            return_value = self.in_order_traversal(root.left)
            return_value.append(root.value)
            return_value = return_value + self.in_order_traversal(root.right)
        return return_value

    # This function return the tree as a list with a root -> left -> right order
    def pre_order_traversal(self, root: Node):
        return_value = []
        if root is not None:
            return_value.append(root.value)
            return_value = return_value + self.pre_order_traversal(root.left)
            return_value = return_value + self.pre_order_traversal(root.right)
        return return_value

    # This function return the tree as a list with a left -> right -> root order
    def post_order_traversal(self, root: Node):
        return_value = []
        if root is not None:
            return_value = self.post_order_traversal(root.left)
            return_value = return_value + self.post_order_traversal(root.right)
            return_value.append(root.value)
        return return_value


list_1 = [1, 5, 2, 4, 8, 9, 0, 5, 3, 8, 10, 6, 14, 11, 17, 13]
tree = Tree(Node(7))

# Insert all items in list_1 to `tree`
for i in list_1:
    tree.insert(Node(i))


# Visit each node of `tree` in `in_order` -> [left -> root -> right] format
print(tree.in_order_traversal(tree.root_node()))
# Visit each node of `tree` in `pre_order` -> [root -> left -> right] format
print(tree.pre_order_traversal(tree.root_node()))
# Visit each node of `tree`s in `post_order` [left -> right -> root] format
print(tree.post_order_traversal(tree.root_node()))

# Print all nodes in `tree`
tree.print_tree(tree.root_node())

# search for if a value exist in the tree
print(tree.search(5, tree.root_node()))
# Result: 5 is True

# search for if a value exist in the tree
print(tree.search(500, tree.root_node()))
# Result: 500 is False
