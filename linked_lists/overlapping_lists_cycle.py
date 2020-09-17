class ListNode():
    def __init__(self, x = 0, next = None):
        self.data = x
        self.next = next

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
            return it # iter is the start of the cycle
    return None # No cycle

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
    return L1

def has_overlap_cycle(L1, L2):
    # Store the start of the cycles
    root1, root2 = has_cycle(L1), has_cycle(L2)

    # Case 1. Both lists don't have cycles
    if not root1 and not root2:
        return has_overlap(L1, L2)
    # Case 2. One list has cycle, the other one does not
    elif (root1 and not root2) or (not root1 and root2):
        return None
    # Case 3. Both lists have cycles
    # Check if cycles overlap
    temp = root2
    while True:
        temp = temp.next
        if temp is root1 or temp is root2:
            break
    # Case 3.1 Cycle don't overlap
    if temp is not root1:
        return None 

    # length of the linked list
    def distance(a,b):
        dis = 0
        while a is not b:
            a = a.next
            dis += 1
        return dis

    # Case 3.2 Cycles overlap
    # Locating overlapping node if they overlap before cycle starts
    # distance to roots because need to find if has_overlap is from start L1 up to root location 
    # otherwise, overlap is inside the cycle
    stem1_len, stem2_len = distance(L1, root1), distance(L2, root2) 
    if stem1_len > stem2_len:
        L2, L1 = L1, L2
        root1, root2 = root2, root1
    for _ in range(abs(stem1_len - stem2_len)):
        L2 = L2.next
    while L1 is not L2 and L1 is not root1 and L2 is not root2 #doesn't matter which point is reached 1st: ==, root1 or root2
        L1, L2 = L1.next, L2.next

    return L1 if L1 is L2 else root1
    
     
    

    
