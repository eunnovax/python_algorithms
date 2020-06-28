
class Node(object):
    def __init__(self, d, next_node=None, prev_node=None):
        self.data = d
        self.next_node = next_node
        self.prev_node = prev_node
    def get_next(self):
        return self.next_node
    def set_next(self, n):
        self.next_node = n
    def get_prev(self):
        return self.prev_node
    def set_prev(self, p):
        self.prev_node = p
    def get_data(self):
        return self.data
    def set_data(self, d):
        self.data = d

class DoublyLinkedList(object):
    def __init__(self, r = None):
        self.root = r
        self.size = 0
    def get_size(self):
        return self.size
    def add(self, d):
        new_node = Node(d, self.root)
        if(self.root == None):
            self.root = new_node
        else:
            self.root.prev_node = new_node
            self.root = new_node
        self.size += 1

dll = DoublyLinkedList()
dll.add(34)
dll.add(9)
print(dll.root.data)
print(dll.root.next_node.data)
print(dll.root.next_node.prev_node.data)