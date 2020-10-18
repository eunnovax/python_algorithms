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

def binary_tree_envelope(tree):
    def is_leaf(node):
        return not node.left and not node.right

    # Computes the left subtree envelope
    def left_subtree_envelope(subtree, is_boundary):
        if not subtree:
            return []
        return (([subtree.data] if is_boundary or is_leaf(subtree) else []) + left_subtree_envelope(subtree.left, is_boundary) + left_subtree_envelope(subtree.right, is_boundary and not subtree.left) )

    # Compute right subtree envelope
    def right_subtree_envelope(subtree, is_boundary):
        if not subtree:
            return []
        return ( right_subtree_envelope(subtree.left, is_boundary and not subtree.right) + right_subtree_envelope(subtree.right, is_boundary) + ([subtree.data] if is_boundary or is_leaf(subtree) else []) )
    
    return ([tree.data] + left_subtree_envelope(tree.left, is_boundary=True) + right_subtree_envelope(tree.right, is_boundary=True) )

tree = BinaryTree(3)
tree.insert(21)
tree.insert(12)
tree.insert(5)
tree.insert(8)
tree.insert(0)
tree.insert(13)
tree.insert(73)
tree.insert(69)
tree.insert(0)
tree.insert(56)
tree.insert(44)

print(binary_tree_envelope(tree.root))