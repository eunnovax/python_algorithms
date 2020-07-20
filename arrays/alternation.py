def rearrange(A):
    for i in range(len(A)):
        A[i:i+2] = sorted(A[i:i+2], reverse = i % 2)
        # print(A[i])
        # print(A[i+1])
        # print(A[i+2])
    return A

arr = [34,1,2,6,45,6,7,78,4,9,10]
print(rearrange(arr))