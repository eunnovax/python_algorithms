class BTNode():
    def __init__(self, data=0):
        self.left = None
        self.right = None
        self.data = data

# O(n) time, O(h) space
def is_symmetric(tree):
    def check_symmetry(subtree1, subtree2):
        # base case
        if not subtree1 and not subtree2:
            return True
        elif subtree1 and subtree2:
            return (subtree1.data == subtree2.data and check_symmetry(subtree1.left, subtree2.right) and check_symmetry(subtree1.right, subtree2.left))
        # One subtree is empty, the other is not
        return False
    return not tree or check_symmetry(tree.left, tree.right)
        
