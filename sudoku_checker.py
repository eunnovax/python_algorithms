import math

def is_valid_sudoku(partial_sudoku):
    n = len(partial_sudoku)
    #check duplicates
    def has_duplicate(block):
        block = list(filter(lambda x: x != 0, block))
        len1 = len(block)
        len2 = len(set(block))
        block = list(filter(lambda x: x <= n, block))
        len3 = len(block)
        return len1 != len2 or len1 != len3

    # check rows and columns
    if any(
        has_duplicate([partial_sudoku[i][j] for j in range(n)]) or has_duplicate([partial_sudoku[j][i] for j in range(n)])
        for i in range(n)
    ):
        return False

    # region squares
    region_size = int(math.sqrt(n))
    return all(not has_duplicate(
        [
            partial_sudoku[a][b] 
            for a in range(region_size*i, region_size*(i+1))
            for b in range(region_size*j, region_size*(j+1))
        ]
    ) for i in range(region_size) for j in range(region_size))

    
sudoku = [[1,2],[3,4]]
print(is_valid_sudoku(sudoku))
# trav = [sudoku[j][0] for j in range(3)]
# n = len(sudoku)
# size = int(math.sqrt(n))
# trav2 = [sudoku[2][b] for b in range(size*1, size*2)]
# print(trav2)
# for a in range(size*1, size*2)