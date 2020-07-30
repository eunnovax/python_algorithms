import random 

def random_sampling(A, k):
    for i in range(k):
        r = random.randint(i, len(A) - 1)
        A[i], A[r] = A[r], A[i]
    return A

def compute_rand_permute(n):
    permutation = list(range(n))
    permutation = random_sampling(permutation, n)
    return permutation

print(compute_rand_permute(5))

#Time: O(n), Space: O(1)