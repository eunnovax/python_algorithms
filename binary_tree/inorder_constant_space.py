def inorder_traversal_constant(tree):  # O(n) time, O(1) space
    prev, result = None, []
    while tree:
        if prev is tree.parent:
            # came down from prev
            if tree.left: # go to the leftmost
                next = tree.left 
            else:
                result.append(tree.data)
                next = tree.right or tree.parent 
        elif tree.left is prev:
            # came down from left child
            result.append(tree.data)
            # go right or up
            next = tree.right or tree.parent 
        else: #done with both childen, move up
            next = tree.parent
        
        prev, tree = tree, next
    return result
