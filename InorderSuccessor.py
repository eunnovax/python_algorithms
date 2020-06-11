from bst_insert_search import BST

def InorderSuccessor(n):
    # Step 1: If node has right subtree
    if n.right is not None:
        return minValue(n.right)

    # Step 2: if node has no right subtree
    p = n.parent
    while(p is not None):
        if (n != p.right):
            break
        n = p 
        p = p.parent
    return p

# Leftmost value search
def minValue(node):
    current = node

    while(current is not None):
        if current.left is None:
            break
        current = current.left
    return current

bst = BST()

bst.insert(2)
bst.insert(3)
bst.insert(10)
bst.insert(7)
bst.insert(11)
bst.insert(19)
bst.insert(1)
print('Root', bst.root)

temp = bst.root.right.right
print('Child node is', temp)

succ = InorderSuccessor(temp)
print('Inorder successor',succ.data)




