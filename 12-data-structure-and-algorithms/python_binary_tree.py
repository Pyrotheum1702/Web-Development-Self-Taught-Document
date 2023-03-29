class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def insert(self, value):
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.insert(value)
            elif value > self.value:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.insert(value)
        else:
            self.value = value

    def search(self, value, node):
        print(node.value)
        if value == node.value:
            return True

        if node.left is not None:
            self.search(value, node.left)

        if node.right is not None:
            self.search(value, node.right)

        return False

    def print_tree(self):
        if self.left is not None:
            self.left.print_tree()
        print(self.value),
        if self.right is not None:
            self.right.print_tree()

# this function return the tree as a list with a left -> root -> right order
    def in_order_traversal(self, root):
        return_value = []
        if root is not None:
            return_value = self.in_order_traversal(root.left)
            return_value.append(root.value)
            return_value = return_value + self.in_order_traversal(root.right)
        return return_value

# this function return the tree as a list with a root -> left -> right order
    def pre_order_traversal(self, root):
        return_value = []
        if root is not None:
            return_value.append(root.value)
            return_value = return_value + self.pre_order_traversal(root.left)
            return_value = return_value + self.pre_order_traversal(root.right)
        return return_value

# this function return the tree as a list with a left -> right -> root order

    def post_order_traversal(self, root):
        return_value = []
        if root is not None:
            return_value = self.post_order_traversal(root.left)
            return_value = return_value + self.post_order_traversal(root.right)
            return_value.append(root.value)
        return return_value


list_1 = [1, 5, 2, 4, 8, 9, 0, 5, 3, 8, 10, 6, 14, 11, 17, 13]
root = Node(7)

# insert all items in list_1 to `root`` tree
for i in list_1:
    root.insert(i)


# visit each node of `root` in `in_order` -> [left -> root -> right] format
print(root.in_order_traversal(root))
# visit each node of `root` in `pre_order` -> [root -> left -> right] format
print(root.pre_order_traversal(root))
# visit each node of `root`s in `post_order` [left -> right -> root] format
print(root.post_order_traversal(root))

# print all nodes in `root` from smallest to largest
root.print_tree()

print(root.search(5, root))
