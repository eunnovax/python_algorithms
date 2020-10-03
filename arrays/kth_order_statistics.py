def nth_order_statistics_quadratic(arr, k):  # O(n*k) < O(n*lon) - for k << n
    for i in range(len(arr)):
        for j in range(k):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i] 
    return arr
    
def partition(arr, start, end):  
    pivot, part_idx = arr[start], start + 1
    # print('pivot', pivot)
    # print('part_idx iter', part_idx)
    for i in range(start + 1, end): # value at index end has alredy been sorted!
        if arr[i] <= pivot:
            arr[i], arr[part_idx] = arr[part_idx], arr[i]
            part_idx += 1
        #     print('part_idx iter', part_idx)
        # print('arr iter', arr)
    arr[part_idx - 1], arr[start] = arr[start], arr[part_idx - 1]
    # print('arr after partition', arr)
    return part_idx - 1

def quickselect(arr, start, end, k): # O(n) time, O(1) space
    k_idx = k - 1
    # print('k_idx', k_idx)
    # print('start', start, ' end', end)
    part_idx = partition(arr, start, end)
    # print('part_idx', part_idx)
    # print('A', arr)
    if part_idx == k_idx:
        print('array at part_idx', arr[part_idx])
        return arr[part_idx]
    elif part_idx < k_idx:
        return quickselect(arr, part_idx + 1, end, k)
    else: # part_idx > k_idx
        return quickselect(arr, start, part_idx, k)

A = [10,6,3,9,8,5,0,45,23]
A1 = [4,0,33,98,1]
print(quickselect(A, 0, len(A), 5))
