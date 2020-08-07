# import numpy as np

def spiral_order(square_matrix):
    def clockwise_matrix_layer(offset):
        # add center element if matrix has odd dimension
        if len(square_matrix) - 2*offset == 1:
            spiral_ordering.append(square_matrix[offset][offset])
            return

        spiral_ordering.extend(square_matrix[offset][offset:-1-offset]) 
        print(spiral_ordering)
        spiral_ordering.extend(list(zip(*square_matrix))[-1-offset][offset:-1-offset])
        print(spiral_ordering)
        spiral_ordering.extend(square_matrix[-1-offset][-1-offset:offset:-1])
        print(spiral_ordering)
        spiral_ordering.extend(list(zip(*square_matrix))[offset][-1-offset:offset:-1])

    spiral_ordering = []
    for offset in range((len(square_matrix) + 1) // 2):
        clockwise_matrix_layer(offset)
    return spiral_ordering

T = [[1,2,3],[4,5,6],[7,8,9]]
print(spiral_order(T))

## Print the 2d array
# for r in T:
#     for c in r:
#         print(c,end = " ")
#     print()
## Print the column of 2d array
# print([row[-1] for row in T])
print([i for i in T[i][-1]])

## Print the transpose of 2d array so that columns become rows
# print(list(zip(*T)))