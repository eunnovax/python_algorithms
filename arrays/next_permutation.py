def next_permutation(P):
    # Find the smallest in suffix > P[inv_point]
    inv_point = len(P) - 2
    while (inv_point >= 0 and P[inv_point] >= P[inv_point + 1]):
        inv_point -= 1
    if inv_point == -1:
        return []

    # Swap 'em
    for i in reversed(range(inv_point + 1, len(P))):
        if P[i] > P[inv_point]:
            P[inv_point], P[i] = P[i], P[inv_point]
            break

    # Suffix in decreasing order
    P[inv_point + 1:] = reversed(P[inv_point + 1:])
    return P

arr = [6,2,1,5,4,3,0]
print(next_permutation(arr))