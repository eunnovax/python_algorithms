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

def binary_tree_from_preorder(preorder):  # O(n) time
    def binary_tree_helper(preorder_iter):
        subtree_key = next(preorder_iter)
        if subtree_key is None:
            return None
        
        left = binary_tree_helper(preorder_iter)
        right = binary_tree_helper(preorder_iter)
        return BTNode(subtree_key, left, right)
    return binary_tree_helper(iter(preorder))

tree = BinaryTree(3)
tree.insert(21)
tree.insert(12)
tree.insert(5)
tree.insert(8)
tree.insert(0)
tree.insert(13)
tree.insert(73)
tree.insert(69)
node1 = tree.root.left.left.data
node2 = tree.root.right.left.data
print(node1)
print(node2)

preorder = [3, 21, 5, 73, None, None, 69, None, None, 8, None, None, 12, 0, None, None, 13, None, None]
tree = binary_tree_from_preorder(preorder)
print(tree.left.left.data)
print(tree.right.left.data)
