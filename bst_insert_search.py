class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, cur_node):
        if data <= cur_node.data:
            if cur_node.left is None:
                cur_node.left = Node(data)
                node = cur_node.left
                node.parent = cur_node
            else:
                self._insert(data, cur_node.left)
        
        elif data > cur_node.data:
            if cur_node.right is None:
                cur_node.right = Node(data)
                node = cur_node.right
                node.parent = cur_node
            else: self._insert(data, cur_node.right)

        else:
            print("Value is already present in tree.")

    def find(self, data):
        if self.root:
            is_found = self._find(data, self.root)
            if is_found:
                return True
            return False
        else: 
            return None

    def _find(self, data, cur_node):
        if data > cur_node.data and cur_node.right:
            return self._find(data, cur_node.right)
        elif data < cur_node.data and cur_node.left:
            return self._find(data, cur_node.left)
        if data == cur_node.data:
            return True

    def height(self):
        final_height = self._height(self.root)
        return final_height

    def _height(self, node):
        if node is None:
            return -1
        left_height = self._height(node.left)
        right_height = self._height(node.right)

        return 1 + max(left_height, right_height)

bst = BST()

bst.insert(4)
bst.insert(20)
bst.insert(2)
bst.insert(10)
bst.insert(5)
bst.insert(7)
bst.insert(9)
print(bst.root.right.left)

# print(bst.find(10))
print(bst.height())

