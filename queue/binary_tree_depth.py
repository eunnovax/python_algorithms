def binary_tree_depth_order(tree):
    result = []
    if not tree:
        return result
    
    nodes_at_current_depth = [tree]
    while nodes_at_current_depth:
        result.append([curr.data for curr in nodes_at_current_depth])
        nodes_at_current_depth = [
            child 
            for curr in nodes_at_current_depth for child in (curr.left, curr.right)
            if child
        ]
    return result

