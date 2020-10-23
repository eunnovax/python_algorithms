import heapq
def find_kth_largest(A, k): # O(nlogk) time, O(k) space
    min_heap = []
    for item in A:
        heapq.heappush(min_heap, item)
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    return heapq.heappop(min_heap)

arr = [2,3,4,1,4,5,1,99,5,0,44]
k = 3
print(find_kth_largest(arr, k))