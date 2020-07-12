def delete_duplicates(A):
    prev, duplicate = 0, 0
    i = 0
    while i < len(A):
        if i == 0:
            prev = A[i]
            i += 1
            continue
        if A[i] == prev:
            A.pop(i)
            prev = A[i-1]
            continue
        prev = A[i]
        i += 1
    print(A)
    return len(A)

def remove_duplicates(A):
    if not A:
        return 0
    
    write_index = 1
    for i in range(1, len(A)):
        if A[write_index - 1] != A[i]:
            A[write_index] = A[i]
            write_index += 1
    return write_index

print(delete_duplicates([13,3,8,8,8,8,8,23,1,1,9]))
