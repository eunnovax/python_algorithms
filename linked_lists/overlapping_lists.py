class ListNode():
    def __init__(self, x = 0, next = None):
        self.data = x
        self.next = next

def has_overlap(L1, L2):
    n1, n2, step1, step2 = L1, L2, 0, 0
    while n1:
        n1 = n1.next
        step1 += 1

    while n2:
        n2 = n2.next
        step2 += 1

    if step2 > step1:
        L2, L1 = L1, L2 # L1 is the longer list
    diff = abs(step1 - step2)
    for _ in range(diff):
        L1 = L1.next
    while L1 and L2 and L2 is not L1:
        L2 = L2.next
        L1 = L1.next
    return L1.data

l1_head = ListNode(0)
l1_tail = l1_head
for i in range(1, 5):
    l1_tail.next = ListNode(i)
    l1_tail = l1_tail.next

l2_head = ListNode(0)
l2_tail = l2_head
for i in range(1, 5):
    l2_tail.next = ListNode(i*2)
    l2_tail = l2_tail.next
l2_tail.next = l1_head.next.next

print(has_overlap(l1_head, l2_head))
