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

# class Ancestor():
#     def __init__(self, node, status):
#         self.node = node
#         self.status = status

def lca(tree, node1, node2):
    Ancestor = collections.namedtuple('Ancestor', ('node','status'))
    def lca_finder(tree, node1, node2):
        # base case
        if not tree:
            return Ancestor(None, 0)
        # visit left
        left = lca_finder(tree.left, node1, node2)
        # print('left', left)
        if left.status == 2:
            return left
        # visit right
        right = lca_finder(tree.right, node1, node2)
        # print('right', right)
        if right.status == 2:
            return right
        # print data
        # print('left status', left.status, 'right status', right.status)
        status = right.status + left.status
        
        if (tree is node1) or (tree is node2):
            status += 1
            print('status inrcemented', status)
        # print('node data', tree.data)
        if status == 2:
            return Ancestor(tree, status)
        else:
            return Ancestor(None, status)
        
    return lca_finder(tree, node1, node2).node.data


tree = BinaryTree(3)
tree.insert(21)
tree.insert(12)
tree.insert(5)
tree.insert(8)
tree.insert(0)
tree.insert(13)
tree.insert(73)
tree.insert(69)

node1 = tree.root.right.right
node2 = tree.root.right.left

print(lca(tree.root, node1, node2))