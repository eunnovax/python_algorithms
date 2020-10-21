import heapq
def online_median(sequence): # O(logn) time per entry for insert extraction
    min_heap, max_heap = [], []
    result = []
    for x in sequence:
        #adds in min_heap, then extracts min from min_heap and adds it to max_heap
        heapq.heappush(max_heap, -heapq.heappushpop(min_heap, x)) 
        #min_heap should have +1 entry when # is odd
        if len(max_heap) > len(min_heap):
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        #compute the median
        result.append(0.5*(min_heap[0] + (-max_heap[0])) if len(min_heap == max_heap) else min_heap[0])
    
    return result