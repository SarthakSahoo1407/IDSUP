def extract_row(matrix, row_index):
    if row_index < 0 or row_index >= len(matrix):
        raise ValueError("Row index out of bounds.")
    return matrix[row_index]

def extract_column(matrix, col_index):
    if col_index < 0 or col_index >= len(matrix[0]):
        raise ValueError("Column index out of bounds.")
    return [row[col_index] for row in matrix]
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
row_1 = extract_row(A, 1)
print("Row 1:", row_1)
col_2 = extract_column(A, 2)
print("Column 2:", col_2)
