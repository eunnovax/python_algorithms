class ListNode():
    def __init__(self, x=0, next=None):
        self.data = x
        self.next = next

def reverse_list(L):  # Time - O(n), Space - O(1)
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

def is_list_palindromic(L):  # Time - O(n), Space - O(1)
    # Finds the second half of the list
    fast = slow = L
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next 
    # Reverse the second half and test for palindromicity
    first, second = L, reverse_list(slow)
    while second and first:
        if second.data != first.data:
            return False
        second, first = second.next, first.next 
    return True 

res_head = ListNode(0)
res_tail = res_head
res_tail.next = ListNode(1)
res_tail = res_tail.next
res_tail.next = ListNode(2)
res_tail = res_tail.next
res_tail.next = ListNode(2)
res_tail = res_tail.next
res_tail.next = ListNode(1)
res_tail = res_tail.next
res_tail.next = ListNode(0)
res_tail = res_tail.next
print(is_list_palindromic(res_head))
