def preorder_traversal(tree): # O(n) time, O(h) space
    stack, result = [tree], []
    while stack:
        d = stack.pop()
        if d:
            result.append(d.data)
            stack += [d.right, d.left]
    return result