def lca(tree, node1, node2):  # O(n) time, O(1) space
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

def lca_parent(node1, node2):  # O(h) time, O(1) space!
    # Compute the height of each node
    height1, height2, temp1, temp2 = 0, 0, node1, node2
    while temp1:
        temp1 = temp1.parent
        height1 += 1
    while temp2:
        temp2 = temp2.parent
        height2 += 1
    # Bring the deeper node to the same depth
    while height1 > height2: # when h1 > h2
        node1 = node1.parent
        height1 -= 1
    while height2 > height1: # when h2 > h1
        node2 = node2.parent
        height2 -= 1
    # Ascension
    while node1 != node2:
        node1, node2 = node1.parent, node2.parent
    return node1
