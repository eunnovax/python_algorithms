import itertools, heapq

def sort_almost_sorted_list(sequence, k): # O(nlogk) time, O(k) space
    result = []
    min_heap = []
    for x in itertools.islice(sequence, k):
        heapq.heappush(min_heap, x)

    for x in sequence[k:len(sequence)]:
        smallest = heapq.heappushpop(min_heap, x)
        result.append(smallest)

    while min_heap:
        smallest = heapq.heappop(min_heap)
        result.append(smallest)
    return result

sequence = [3,-1,2,6,4,5,8]
s2 = [3,-1, 2, 7,6,5]
k = 2
print(sort_almost_sorted_list(s2, k))