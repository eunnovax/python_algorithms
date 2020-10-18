class BTNode():
    def __init__(self, data=0, left=None, right=None, rsibling=None):
        self.data, self.left, self.right, self.rsibling = data, left, right, rsibling

def right_sibling(tree):
    def populate_next_field(node): # level traversal
        while node and node.left:
            node.left.next = node.right
            node.right.next = node.next and node.next.left 
            node = node.next
    while tree and tree.left: # depth traversal
        populate_next_field(tree)
        tree = tree.left
