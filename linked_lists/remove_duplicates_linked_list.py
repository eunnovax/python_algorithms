class ListNode():
    def __init__(self, x=0, next=None):
        self.data = x
        self.next = next

def remove_duplicates(L):
    tail = L
    print('tail', tail, ' L', L)
    while tail and tail.next:
        if tail.data == tail.next.data:
            tail.next = tail.next.next
        tail = tail.next
    return L

# Time - O(n), Space O(1)

res_head = ListNode(0)
res_tail = res_head
res_tail.next = ListNode(2)
res_tail = res_tail.next
res_tail.next = ListNode(2)
res_tail = res_tail.next
res_tail.next = ListNode(3)
res_tail = res_tail.next
res_tail.next = ListNode(5)
res_tail = res_tail.next
res_tail.next = ListNode(7)
res_tail = res_tail.next
res_tail.next = ListNode(11)
res_tail = res_tail.next
res_tail.next = ListNode(11)
res_tail = res_tail.next
l = remove_duplicates(res_head)

while l:
    print(l.data)
    l = l.next

    

        