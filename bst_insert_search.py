class Queue(object):
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)

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

    # def print_bst(self, traversal_type):
    #     if traversal_type == "levelorder":
    #         return self.levelorder_print(bst.root)
        

    def levelorder_print(self):
        if self.root is None:
             return
        
        queue = Queue()
        queue.enqueue(self.root)
        # traversal = ""
        while not queue.is_empty():
            # traversal += str(queue.peek()) + "-"
            node = queue.dequeue()
            print(node.data)
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        # return traversal

    # in-class inorder traversal with complexity O(n) 
    def inorder_print_tree(self):
        if self.root:
            self._inorder_print_tree(self.root)

    def _inorder_print_tree(self, cur_node):
        if cur_node:
            self._inorder_print_tree(cur_node.left)
            print(str(cur_node.data))
            self._inorder_print_tree(cur_node.right)

    def is_bst_valid(self):
        if self.root:
            is_valid = self._is_bst_valid(self.root, self.root.data)

            if is_valid is None:
                return True
            return False
        return True

    def _is_bst_valid(self, cur_node, data):
        if cur_node.left:
            if data > cur_node.left.data:
                return self._is_bst_valid(cur_node.left, cur_node.left.data)
            else:
                return False
        if cur_node.right:
            if data < cur_node.right.data:
                return self._is_bst_valid(cur_node.right, cur_node.right.data)
            else:
                return False 

    def findMin(self):
        if(self.root == None):
            return -1
        root = self.root
        while(root.left != None):
            root = root.left
        return root.data

    def findMax(self):
        if(self.root == None):
            return -1
        root = self.root
        while(root.right != None):
            root = root.right
        return root.data 

bst = BST()

bst.insert(4)
bst.insert(20)
bst.insert(2)
bst.insert(10)
bst.insert(5)
bst.insert(7)
bst.insert(9)
# print(bst.root.right.left)
# print(bst.find(10))
# print(bst.height())
# print(bst.inorder_print_tree())

#   1
#  2 3
# tree = BST()
# tree.root = Node(1)
# tree.root.left = Node(2) 
# tree.root.right = Node(3)

# print(tree.inorder_print_tree())
# print(bst.is_bst_valid())
# print(tree.is_bst_valid())
# print('bst minimum is', bst.findMin())
# print('bst maximum is', bst.findMax())
print(bst.levelorder_print())

