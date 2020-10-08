import collections

class BTNode():
    def __init__(self, data=0):
        self.left = None
        self.right = None
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

def sum_r2l(tree):
    def sum_root_to_leaf(tree):
        Sum = collections.namedtuple('Sum', ('data', 'sum'))
        # base case
        if not tree:
            return Sum(0, 0)
        # left
        left = sum_root_to_leaf(tree.left)
        print('left sum', left.sum)
        # right
        right = sum_root_to_leaf(tree.right)
        print('right sum', right.sum)
        # print
        partial_sum = (left.sum + right.sum) * 2 + (left.data + right.data)  # in-level summation and base conversion
        return Sum(tree.data, partial_sum)
    # divide by 4 in the end
    return (sum_root_to_leaf(tree).sum) / 4

def sum_root_to_laef_correct(tree, p_s=0):  # O(n) time and O(h) space
    if not tree:
        return 0
    p_s = p_s * 2 + tree.data 
    if not tree.left and not tree.right: #Leaf
        return p_s
    # Non-leaf
    return (sum_root_to_laef_correct(tree.left, p_s) + sum_root_to_laef_correct(tree.right, p_s))

tree = BinaryTree(0)
tree.insert(1)
tree.insert(1)
tree.insert(0)
tree.insert(1)
tree.insert(0)
tree.insert(1)
tree.insert(0)
tree.insert(1)

print(sum_root_to_laef_correct(tree.root))