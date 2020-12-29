class Node:

    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self.insert_node(data, self.root)

    # Time complexity: O(logN)
    def insert_node(self, data, node: Node):
        if data < node.data:
            if node.left_child:
                self.insert_node(data, node.left_child)
            else:
                node.left_child = Node(data)
        else:
            if node.right_child:
                self.insert_node(data, node.right_child)
            else:
                node.right_child = Node(data)

    def get_min_value(self):
        if self.root:
            return self.get_min(self.root)

    def get_min(self, node: Node):
        if node.left_child:
            return self.get_min(node.left_child)
        return node.data

    def get_max_value(self):
        if self.root:
            return self.get_max(self.root)

    def get_max(self, node: Node):
        if node.right_child:
            return self.get_min(node.right_child)
        return node.data

    def traverse(self):
        if self.root:
            self.traverse_in_order(self.root)

    def traverse_in_order(self, node:Node):
        if node.left_child:
            self.traverse_in_order(node.left_child)
        if node.right_child:
            self.traverse_in_order(node.right_child)
