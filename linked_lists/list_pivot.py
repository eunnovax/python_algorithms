class ListNode():
    def __init__(self, x=0, next=None):
        self.data = x
        self.next = next

def list_pivoting(L, k):
    less_head = less_iter = ListNode()
    equal_head = equal_iter = ListNode()
    greater_head = greater_iter = ListNode()

    # Populate the three lists
    while L:
        if L.data < k:
            less_iter.next = L
            less_iter = less_iter.next
        elif L.data == k:
            equal_iter.next = L
            equal_iter = equal_iter.next
        else: #L.data > k
            greater_iter.next = L
            greater_iter = greater_iter.next
        L = L.next
    # Combine three lists
    greater_iter.next = None
    equal_iter.next = greater_head.next
    less_iter.next = equal_head.next
    return less_head.next

# Time - O(n), Space - O(1)

res_head = ListNode(2)
res_tail = res_head
res_tail.next = ListNode(7)
res_tail = res_tail.next
res_tail.next = ListNode(5)
res_tail = res_tail.next
res_tail.next = ListNode(10)
res_tail = res_tail.next
res_tail.next = ListNode(3)
res_tail = res_tail.next
res_tail.next = ListNode(1)
res_tail = res_tail.next
res_tail.next = ListNode(7)
res_tail = res_tail.next
sorted_list = list_pivoting(res_head, 7)
while sorted_list.next:
    print("sorted list", sorted_list.data)
    sorted_list = sorted_list.next
print("sorted list", sorted_list.data)