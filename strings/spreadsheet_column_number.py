import functools

def ss_column_id(col):
    col_id = functools.reduce(lambda sum, c: sum*26 + ord(c)- ord('A') + 1, col, 0)
    return col_id

column = 'AA'
print(ss_column_id(column))