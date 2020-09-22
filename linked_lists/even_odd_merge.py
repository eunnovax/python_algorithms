class ListNode():
    def __init__(self, x=0, next=None):
        self.data = x
        self.next = next

def even_odd_merge(L):
    dummy_head = ListNode(0, L)
    even = dummy_head.next
    odd_one = odd = dummy_head.next.next
    while odd.next and odd.next.next:
        even.next, odd.next = odd.next, odd.next.next
        even = even.next
        odd = odd.next
    if odd.next is None:
        even.next = odd_one
    else:
        even.next = odd.next
        odd.next = None
        even.next.next = odd_one
    return dummy_head.next

ll_head = ListNode(0)
ll_tail = ll_head
for i in range(1, 6):
    ll_tail.next = ListNode(i)
    ll_tail = ll_tail.next
    print("initial list", ll_tail.data)
even_odd = even_odd_merge(ll_head)
while even_odd.next:
    even_odd = even_odd.next
    print("new list", even_odd.data)

# print(even_odd.data)
# print(even_odd.next.data)        
# print(even_odd.next.next.data)        
# print(even_odd.next.next.next.data)   
# print(even_odd.next.next.next.next.data)        

#Time - O(n), Space - O(1)
            