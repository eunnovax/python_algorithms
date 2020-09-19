class ListNode():
    def __init__(self, x = 0, next = None):
        self.data = x
        self.next = next

def remove_kth_last(L, k):
    n1, n2, length = L, L, 0
    while n1 != None:
        n1 = n1.next
        length += 1
    dis = length - k
    it = 0
    while it < dis:
        n2 = n2.next
        it += 1
    n2.next = n2.next.next
    return n2

# Two iterators. One starts at k and reaches the end when second reaches kth element
def remove_kth_last_fast(L, k):
    dummy_head = ListNode(0, L)
    first  = dummy_head.next
    for _ in range(k):
        first = first.next

    second = dummy_head
    while first:
        first, second = first.next, second.next
    # second points to (k+1)th last node (one before k)
    second.next = second.next.next
    return second.next 