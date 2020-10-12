def find_successor(node): #O(h) time
    # right subtree
    if node.right:
        node = node.right        
        while node:
            node = node.left
        return node.parent
    # no right subtree
    # find closest ancestor whose left subtree contains node
    while node.parent and node.parent.right is node:
        node = node.parent
    # node.parent is None => node is the rightmost node in the tree
    return node.parent