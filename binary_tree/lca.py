def lca(tree, node1, node2):
    Ancestor = collections.namedtuple('Ancestor', ('node','status'))
    def lca_finder(tree, node1, node2):
        # base case
        if not tree or tree is node1 or tree is node2:
            return Ancestor(None, 'not found')
        # visit left
        left = lca_finder(tree.left, node1, node2)
        if left.status == 'found':
            return left
        # visit right
        right = lca_finder(tree.right, node1, node2)
        if right.status == 'found':
            return right
        # print data
        if left.node is right.node:
            return Ancestor(left.node, 'found')
        else:
            return Ancestor(tree, 'not found')
        
    return lca_finder(tree, node1, node2).node

