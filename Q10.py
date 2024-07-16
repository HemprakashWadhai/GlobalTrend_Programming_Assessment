#10. Write a Python function that takes a 2D list (matrix) and returns its transpose.
def transpose_matrix(matrix):
    # Calculate dimensions of the input matrix
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    
    # Initialize an empty transposed matrix
    transposed = []
    
    # Iterate through columns of original matrix
    for col in range(cols):
        transposed_row = []
        # Iterate through rows of original matrix
        for row in range(rows):
            # Add the element at the current (row, col) to transposed matrix
            transposed_row.append(matrix[row][col])
        # Add the transposed row to the transposed matrix
        transposed.append(transposed_row)
    
    return transposed

# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Original Matrix:")
for row in matrix:
    print(row)

transposed_matrix = transpose_matrix(matrix)

print("\nTransposed Matrix:")
for row in transposed_matrix:
    print(row)
