class ListNode():
    def __init__(self, x = 0, next = None):
        self.data = x
        self.next = next

# Assume node to delete is not tail
def delete_from_list(node_del):
    node_del.data = node_del.next.data 
    node_del.next = node_del.next.next

# Time - O(1)