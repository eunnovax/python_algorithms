def is_balanced_tree(tree):
    BalancedWithHeight = collections.namedtuple('BalancedWithHeight', ('balanced', 'height'))

    def check_balance(tree):
        # Base case
        if not tree:
            return BalancedWithHeight(True, -1)
        
        # Implement Postorder traversal
        # left subtree
        left_tree = check_balance(tree)
        if not left_tree.balanced:
            # not balanced
            return BalancedWithHeight(False, 0)

        # right subtree
        right_tree = check_balance(tree)
        if not right_tree.balanced:
            # not balanced
            return BalancedWithHeight(False, 0)

        # data operation - balance & height check
        is_balanced = abs(left_tree.height - right_tree.height) <= 1
        height = max(left_tree.height, right_tree.height) + 1
        return BalancedWithHeight(is_balanced, height)

    return check_balance(tree).balanced 