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

def longest_increasing_sequence(tree):
    def longest_sequence_helper(tree, countl, countr):
        if not tree:
            return max(countl, countr)
        if (tree.left and tree.left.data > tree.data):
            countl += 1
        left = longest_sequence_helper(tree.left, countl, countr)
        if (tree.right and tree.right.data > tree.data):
            countr += 1
        right = longest_sequence_helper(tree.right, countl, countr)

        return max(left, right)
    return longest_sequence_helper(tree, 0,0 )

tree = BinaryTree(3)
tree.insert(21)
tree.insert(12)
tree.insert(5)
tree.insert(8)
tree.insert(15)
tree.insert(13)
tree.insert(73)
tree.insert(69)
tree.insert(0)
tree.insert(56)
tree.insert(44)

print(longest_increasing_sequence(tree.root))