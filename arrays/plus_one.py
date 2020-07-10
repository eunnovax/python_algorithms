# Program which takes as input an array of digits encoding a nonnegative decimal integer D and updates the array to represent the integer D + 1.
def plus_one(A):
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i - 1] += 1
    if A[0] == 10:
        # If there is a carry out, add 0 to the last digit, and 1 to the 1st entry.
        A[0] = 1
        A.append(0)
    return A