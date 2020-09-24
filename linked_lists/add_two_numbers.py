class ListNode():
    def __init__(self, x=0, next=None):
        self.data = x
        self.next = next

def add_two_numbers(L1, L2):
    carryout = 0
    L_head = ListNode()
    L_tail = L_head
    while L1 or L2 or carryout: # loop until both reach None
        sum = L1.data + L2.data + carryout
        if sum > 9:
            carryout = sum // 10
            sum = sum % 10
        L_tail.next = ListNode(sum)
        L_tail, L1, L2 = L_tail.next, L1.next, L2.next
    return L_head.next

ll_head1 = ListNode(0)
ll_head2 = ListNode(0)
ll_tail1 = ll_head1
ll_tail2 = ll_head2
for i in range(1, 4):
    ll_tail1.next = ListNode(i)
    ll_tail1 = ll_tail1.next
    ll_tail2.next = ListNode(i)
    ll_tail2 = ll_tail2.next
    print("initial list", ll_tail1.data)

sum_list = add_two_numbers(ll_head1, ll_head2)
while sum_list.next:
    print("reversed node", sum_list.data)
    sum_list = sum_list.next
print("reversed node", sum_list.data)


    
