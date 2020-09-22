class ListNode():
    def __init__(self, x=0, next=None):
        self.data = x
        self.next = next

def reverse_list(L):
    dummy_head = L
    prev = None
    current = dummy_head
    while current:
        nnext = current.next
        current.next = prev
        prev = current
        current = nnext
    dummy_head = prev
    return dummy_head

ll_head = ListNode(0)
ll_tail = ll_head
for i in range(1, 6):
    ll_tail.next = ListNode(i)
    ll_tail = ll_tail.next
    print("initial list", ll_tail.data)
reversedList = reverse_list(ll_head)
while reversedList.next:
    print("reversed node", reversedList.data)
    reversedList = reversedList.next
print("reversed node", reversedList.data)
