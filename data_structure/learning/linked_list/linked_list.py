class Node(object):
    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList(object):

    def __init__(self):
        self.head: Node = None
        self.size = 0

    # time complexity = O(1)
    def insert_start(self, data):
        self.size += 1
        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def size(self):
        return self.size

    # time complexity = O(N)
    def insert_end(self, data):
        self.size +=1
        new_node = Node(data)
        actual_node = self.head

        while actual_node.next_node is not None:
            actual_node = actual_node.next_node

        actual_node.next_node = new_node

    # time complexity = O(N)
    def traverse_list(self):
        actual_node = self.head

        while actual_node is not None:
            print("{} - ".format(actual_node.data))
            actual_node = actual_node.next_node



