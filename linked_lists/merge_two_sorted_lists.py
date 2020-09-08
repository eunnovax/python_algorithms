class ListNode():
    def __init__(self, x = 0):
        self.data = x
        self.next = None

def merge_sorted_lists(L1, L2):
    d_head = tail = ListNode()

    while L1 and L2:
        if L1.data < L2.data:
            # assign the smallest value to the new list
            # refill the smallest value position with the next node
            tail.next, L1 = L1, L1.next
        else:
            tail.next, L2 = L2, L2.next
        tail = tail.next
    #Appends the remaining nodes of L1, L2
    tail.next = L1 or L2
    return d_head.next.next.next.next.data

res_head = ListNode(0)
res_tail = res_head
res_tail.next = ListNode(1)
res_tail = res_tail.next
res_tail.next = ListNode(2)
res_tail = res_tail.next
print(res_head.next.next.data)

res_head2 = ListNode(3)
res_tail2 = res_head2
res_tail2.next = ListNode(10)
res_tail2 = res_tail2.next
res_tail2.next = ListNode(22)
res_tail2 = res_tail2.next
print(res_head2.next.next.data)
print(merge_sorted_lists(res_head, res_head2))