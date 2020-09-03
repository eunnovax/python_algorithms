def rotate_matrix(square_matrix):
    matrix_size = len(square_matrix) - 1
    for i in range(len(square_matrix) // 2):
        for j in range(i, matrix_size - i):
            # 4 - way exchange on the outer layer
            # A[~i] == A[-(i+1)]
            print('1st', square_matrix[i][j])
            print('2nd', square_matrix[~j][i])
            (square_matrix[i][j], square_matrix[~j][i], square_matrix[~i][~j], square_matrix[j][~i]) = (square_matrix[~j][i], square_matrix[~i][~j], square_matrix[j][~i], square_matrix[i][j])
    return square_matrix

def rotate_2d_array(matrix):
    matrix = list(zip(*matrix))
    for i in range(len(matrix)):
        matrix[i] = list(reversed(matrix[i]))
    return matrix


matr = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(rotate_2d_array(matr))
print(rotate_matrix(matr))