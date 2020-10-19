import heapq

def merge_sorted_arrays(sorted_lists): # O(nlogk) time, O(k) space
    min_heap = []
    sorted_lists_iters = [iter(x) for x in sorted_lists] # list of iterators for each array
    # initialize min_heap with 1st elements from each list
    for i, it in enumerate(sorted_lists_iters):
        first_element = next(it, None)
        if first_element is not None:
            heapq.heappush(min_heap, (first_element, i))
    
    # populate the sorted array by processing through min_heap
    result = []
    while min_heap:
        smallest_entry, smallest_entry_idx = heapq.heappop(min_heap)
        smallest_iter = sorted_lists_iters[smallest_entry_idx]
        result.append(smallest_entry)
        next_element = next(smallest_iter, None)
        if next_element is not None:
            heapq.heappush(min_heap, (next_element, smallest_entry_idx))
    return result
