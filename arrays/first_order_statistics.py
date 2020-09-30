def nth_order_statistics(arr, k):  # O(n*k) < O(n*lon) - for k << n
    for i in range(len(arr)):
        for j in range(k):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i] 
    return arr

array = [10,6,3,9,8,5,0,45,23]
print(nth_order_statistics(array, 5))