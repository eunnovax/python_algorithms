import random 

def random_sampling(A, k):
    for i in range(k):
        r = random.randint(i, len(A) - 1)
        A[i], A[r] = A[r], A[i]
    return A

arr = [3,2,0,5,8]
print(random_sampling(arr, 4))

# Time: O(k), Space: O(1)