def lca(tree, node1, node2):
    def lca_finder(tree, node1, node2):
        # base case
        if tree is node1 or tree is node2:
            return tree
        # visit left
        left = lca_finder(tree.left, node1, node2)
        # visit right
        right = lca_finder(tree.right, node1, node2)
        # print data
        if left is not right:
            return tree
        elif left is right:
            return left
    return lca_finder(tree, node1, node2)

