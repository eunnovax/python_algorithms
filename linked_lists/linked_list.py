import logging
from copy import copy, deepcopy

logging.basicConfig(filename='myLinkedListLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug('Start of the program')

class Node(object):
    def __init__  (self, d, n = None):
        self.data = d
        self.next_node = n
    def get_next (self):
        return self.next_node
    def set_next (self, n):
        self.next_node = n
    def get_data(self):
        return self.data
    def set_data(self, d):
        self.data = d

class LinkedList(object):
    def __init__(self, r = None):
        self.root = r
        self.size = 0
    def get_size(self):
        return self.size
    def add(self, d):
        new_node = Node(d, self.root)
        self.root = new_node
        self.size += 1
    def remove(self, d):
        this_node = self.root
        prev_node = None
        while this_node:
            if this_node.get_data() == d:
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node.get_next()
                self.size -= 1
                return True # data removed
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False

    def find(self, d):
        this_node = self.root
        while this_node:
            if this_node.get_data() == d:
                return d
            else:
                this_node = this_node.get_next()
        return None

    def update(self, d, rd):
        this_node = self.root
        prev_node = None
        while this_node:
            if this_node.get_data() == rd:
                new_node = Node(d, this_node.get_next())
                if prev_node:
                    prev_node.set_next(new_node)
                    del this_node
                else:
                    self.root = new_node
                    del this_node
                return True
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False

    def reverse(self):
        logging.debug('Head of LL %s' % (self.root.data))
        this_node = self.root
        prev_node = None
        while this_node:
            temp_node = deepcopy(this_node)
            if this_node.get_next() is None:
                logging.debug('This node next data is None')
            else:
                logging.debug('This node next data is %s' % (this_node.get_next().data))
            if prev_node:
                temp_node.set_next(prev_node)
                logging.debug('Temp next node is %s' % (temp_node.get_next().data))
            else:
                temp_node.set_next(None)
                logging.debug('Temp next node is %s' % (temp_node.get_next()))
            prev_node = temp_node
            logging.debug('Prev node is %s' % (prev_node.get_data()))
            logging.debug('This node next is %s' % (this_node.get_next()))
            this_node = this_node.get_next()
        self.root = prev_node
        logging.debug('Head node is %s' % (self.root.data))
        return True

def merge_sorted_lists(L1, L2):
    d_head = tail = LinkedList()

    while L1 and L2:
        if L1.data < L2.data:
            tail.next, L1 = L1, L1.next
        else:
            tail.next, L2 = L2, L2.next
        tail = tail.next
    #Appends the remaining nodes of L1, L2
    tail.next = L1 or L2
    return d_head.next


ll = LinkedList()
ll.add(4)
ll.add(3)
ll.add(40)
ll.add(23)
# print(ll.size)
# ll.remove(23)
# print(ll.remove(40))
# print(ll.size)
# print(ll.find(40))
# print(ll.update(50, 3))
# print(ll.root.data)
# print(ll.root.next_node.data)
# print(ll.root.next_node.next_node.data)
# print(ll.root.next_node.next_node.next_node.data)
# print(ll.root.next_node.next_node.next_node.next_node)
print(ll.reverse())
print(ll.root.data)
print(ll.root.next_node.data)
print(ll.root.next_node.next_node.data)
print(ll.root.next_node.next_node.next_node.data)

