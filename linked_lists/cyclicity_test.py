class ListNode():
    def __init__(self, x = 0, next = None):
        self.data = x
        self.next = next

def test_cyclicity_hash(L): # Time O(n), Space O(n)
    h = set()
    while not(L == None or L in h):
        # print(L.data)
        h.add(L)
        L = L.next
    if L == None:
        return None
    else:
        return L.data

# Floyd's Cycle Detection Algorithm (Hare algorithm)
def has_cycle(head): # Time O(n) - O(F) (F - # of nodes to the cycle start), Space O(1)
    # Count the length of the cycle
    def cycle_len(meetpoint):
        start, step = meetpoint, 0
        while True:
            step += 1
            start = start.next
            if start is meetpoint:
                return step
    
    fast = slow = head
    while fast and fast.next and fast.next.next:
        slow, fast = slow.next, fast.next.next
        # print('slow', slow.data, ' fast', fast.data)
        if slow is fast:
            # Get to the fast-slow meet point
            cycle_iter = head
            for _ in range(cycle_len(slow)):
                cycle_iter = cycle_iter.next
            
            # Find the start of the cycle
            it = head
            while it is not cycle_iter:
                it = it.next
                cycle_iter = cycle_iter.next
            return it.data # iter is the start of the cycle
    return None # No cycle

ll_head = ListNode(0)
ll_tail = ll_head
for i in range(1, 15):
    ll_tail.next = ListNode(i)
    ll_tail = ll_tail.next
ll_tail.next = ll_head.next.next.next
print(test_cyclicity_hash(ll_head)) 
print(has_cycle(ll_head))


    