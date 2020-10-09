def find_kth_node_inorder(tree, k):  # O(h) time
    while tree:
        left_size = tree.left.size if tree.left else 0
        if left_size + 1 < k: # kth node in the right subtree
            k -= left_size + 1
            tree = tree.right
        elif left_size + 1 == k: # kth node is iter itself
            return tree
        else: # kth node in the left subtree
            tree = tree.left 
    return None # if k is b/w 1 and tree size, this is unreachable


