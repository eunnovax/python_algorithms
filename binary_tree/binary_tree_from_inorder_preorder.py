class BTNode():
    def __init__(self, data=0, left = None, right=None):
        self.left = left
        self.right = right
        self.data = data

class BinaryTree(): # fills nodes left-to-right using queue
    def __init__(self, data=0):
        self.root = BTNode(data)
    
    def insert(self, data):
        if not self.root:
            self.root = BTNode(data)
            return
        q = []
        q.append(self.root)
        # level order traversal until we find an empty place
        while q:
            temp = q[0]
            q.pop(0)
            # Insert node as the left child of the parent node.
            if not temp.left:
                temp.left = BTNode(data) 
                break
            # If the left node is not null push it to the queue.
            else:
                q.append(temp.left)
            # Insert node as the right child of the parent node.
            if not temp.right:
                temp.right = BTNode(data)
                break
            # If the right node is not null push it to the queue.
            else:
                q.append(temp.right)

# class TreeData():
#     def __init__(self, p_idx, i_idx, tree):
#         self.p_idx, self.i_idx, self.tree = p_idx, i_idx, tree

# def binary_tree_from_preorder_inorder(preorder, inorder):
#     # hashtable of parents
#     parent = {}
#     # root
#     tree = BTNode(preorder[0])
#     temp, p_idx, i_idx = tree, 0, 0
#     treeData = TreeData(p_idx, i_idx, temp)
#     def binary_tree_helper(p_idx, preorder, i_idx, inorder, temp):
#         # exit case
#         if p_idx > len(preorder)-1 or i_idx > len(inorder)-1:
#             return temp
#         # 1. check if left subtree
#         # 2. if no left subtree => fill right subtree 
#         if preorder[p_idx] == inorder[i_idx]: # no left subtree 
#             # check for right subtree
#             i_idx += 1
#             p_idx += 1
#             if preorder[p_idx] == inorder[i_idx]: # right subtree exists    
#                 temp.right = BTNode(preorder[p_idx])
#                 temp = temp.right
#                 print('tree entry - right child')
#             binary_tree_helper(p_idx, preorder, i_idx, inorder, temp)
#         # 3. if left subtree => fill left subtree => return leftmost parent
#         treeData = left_subtree(temp, p_idx, preorder, i_idx, inorder, parent)
#         print('leftmost parent', treeData.tree.data)
#         # increment after filling tree
#         treeData.p_idx += 1
#         treeData.i_idx += 1
#         # print('preorder current element', preorder[treeData.p_idx])
#         # print('inorder current element', inorder[treeData.i_idx])
#         # 4. after-leftmost-next-is-parent-or-right-child subroutine => return right child
#         treeData = parent_or_right_child(treeData.tree, treeData.p_idx, preorder, treeData.i_idx, inorder, parent) 
#         print('right child', treeData.tree.data)
#         # 5. recurse
#         return binary_tree_helper(treeData.p_idx, preorder, treeData.i_idx, inorder, treeData.tree)

#         # if next is parent or right child subroutine
#     def parent_or_right_child(temp, p_idx, preorder, i_idx, inorder, parent):
#         if p_idx > len(preorder)-1 or i_idx > len(inorder)-1:
#             return TreeData(p_idx, i_idx, temp)
#         # print('inorder at ', [i_idx], ' = ', inorder[i_idx] )
#         # print('temp.data', temp.data)
#         if inorder[i_idx] == temp.data: #next is parent => go up until right child exists
#             # print('parent of temp', parent[temp].data)
#             return parent_or_right_child(parent[temp], p_idx, preorder, i_idx + 1, inorder, parent)
#         else:
#             temp.left.right = BTNode(preorder[p_idx])
#             print('tree entry - right child', temp.left.right.data)
#             td = TreeData(p_idx, i_idx, temp.left.right)
#             return td

#     def left_subtree(temp, p_idx, preorder, i_idx, inorder, parent):
#         if p_idx > len(preorder) - 1 or i_idx > len(inorder) - 1:
#             return TreeData(p_idx, i_idx, temp)
#         while p_idx < len(preorder) and i_idx < len(inorder) and preorder[p_idx] != inorder[i_idx]: #while preorder is not local/global leftmost
#             temp.left = BTNode(preorder[p_idx]) 
#             p_idx += 1
#             # print('p_idx in LS', p_idx )
#             parent[temp.left] = temp 
#             temp = temp.left
#             print('tree entry', temp.data)

#         temp.left = BTNode(preorder[p_idx])
#         print('tree entry - leftmost', temp.left.data)
#         return TreeData(p_idx, i_idx, temp)


#     binary_tree_helper(treeData.p_idx, preorder, treeData.i_idx, inorder, treeData.tree)
#     return treeData.tree

def binary_tree_from_preorder_inorder(preorder, inorder):
    node_to_inorder_idx = {data: i, for i, data in enumerate(inorder)}

    def binary_tree_helper(preorder_start, preorder_end, inorder_start, inorder_end):
        if preorder_start >= preorder_end or inorder_start >= inorder_end:
            return None
        
        root_inorder_idx = node_to_inorder_idx[preorder[preorder_start]]
        left_subtree_size = root_inorder_idx - inorder_start
        return BTNode(
            preorder[preorder_start],
            binary_tree_helper(preorder_start+1, preorder_start+1+left_subtree_size, inorder_start, root_inorder_idx),
            binary_tree_helper(preorder_start+1+left_subtree_size, preorder_end, root_inorder_idx+1, inorder_end)
        )
    return binary_tree_helper(0, len(preorder), 0, len(inorder))

tree = BinaryTree(3)
tree.insert(21)
tree.insert(12)
tree.insert(5)
tree.insert(8)
tree.insert(0)
tree.insert(13)
tree.insert(73)
tree.insert(69)

node1 = tree.root.left.left.data
node2 = tree.root.right.left.data
# print(node1)
# print(node2)

inorder = [73, 5, 69, 21, 8, 3, 0, 12, 13]
preorder = [3, 21, 5, 73, 69, 8, 12, 0, 13]

r = binary_tree_from_preorder_inorder(preorder, inorder)
# print(r.data)
# print(r.right.left.data)