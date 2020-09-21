class ListNode():
    def __init__(self, x=0, next=None):
        self.data = x
        self.next = next

# Two iterators method: Time - O(n), Space - O(1)
def cyclic_right_shift(L, k):
    dummy_head = ListNode(0, L)
    first = dummy_head.next
    for _ in range(k):
        first = first.next
    second = dummy_head
    while first.next:
        print("first", first.data)
        first, second = first.next, second.next
    first.next = dummy_head.next
    dummy_head.next = second.next.next
    second.next.next = None
    first = dummy_head.next
    return dummy_head

ll_head = ListNode(0)
ll_tail = ll_head
for i in range(1, 5):
    ll_tail.next = ListNode(i)
    ll_tail = ll_tail.next
    print("initial list", ll_tail.data)
new_head = cyclic_right_shift(ll_head, 2)
# print("new head", new_head.next.data)
# print("new head", new_head.next.next.data)
# print("new head", new_head.next.next.next.data)

while new_head.next:
    new_head = new_head.next
    print("new list", new_head.data)