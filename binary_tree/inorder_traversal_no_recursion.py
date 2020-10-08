def inorder_traversal(tree):  # O(n) time, O(h) space
    stack, result = [], []
    while stack or tree:
        if tree:
            stack.append(tree)
            # left
            tree = tree.left
        else:
            # print data
            tree = stack.pop()
            result.append(tree.data)
            # right
            tree = tree.right        