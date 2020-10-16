class BTNode():
    def __init__(self, data=0, left = None, right=None):
        self.left = left
        self.right = right
        self.data = data

class BinaryTree(): # fills nodes left-to-right using queue
    def __init__(self, data=0):
        self.root = BTNode(data)
    
    def insert(self, data):
        if not self.root:
            self.root = BTNode(data)
            return
        q = []
        q.append(self.root)
        # level order traversal until we find an empty place
        while q:
            temp = q[0]
            q.pop(0)
            # Insert node as the left child of the parent node.
            if not temp.left:
                temp.left = BTNode(data) 
                break
            # If the left node is not null push it to the queue.
            else:
                q.append(temp.left)
            # Insert node as the right child of the parent node.
            if not temp.right:
                temp.right = BTNode(data)
                break
            # If the right node is not null push it to the queue.
            else:
                q.append(temp.right)

class LinkedList():
    def __init__(self, data=0, next=None):
        self.data, self.next = data, next

def linked_list_from_tree(tree):
    # base case
    if not tree:
        return []
    if tree.left is None and tree.right is None:
        return [tree.data]
    
    left = linked_list_from_tree(tree.left)
    right = linked_list_from_tree(tree.right)
    return left + right # list concatenation

tree = BinaryTree(3)
tree.insert(21)
tree.insert(12)
tree.insert(5)
tree.insert(8)
tree.insert(0)
tree.insert(13)
tree.insert(73)
tree.insert(69)

print(linked_list_from_tree(tree.root))
