
def permute_app(P, A):
    for i in range(len(A)):
        # check if elem at i has not been moved by checking if
        # P[i] >= 0
        next = i
        while P[next] >= 0:
            A[i], A[P[next]] = A[P[next]], A[i]
            temp = P[next]
            # Subtracts len(P) from an entry in P to make it negative,
            # which indicates the corresponding move has been performed
            P[next] -= len(P)
            next = temp
    P[:] = [aa + len(P) for aa in P]
    return A

perm = [3,2,1,0]
arr = [34,1,2,6]
print(permute_app(perm, arr))