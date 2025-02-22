
def transpose(matrix):
    transpose = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0])) ]
    for  row in range(len(matrix)): 
        for col in range(len(matrix[0])): 
            transpose[col][row] = matrix[row][col]
    return transpose
    

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(transpose(matrix))

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(transpose(matrix))


# Problem 1: Transpose Matrix
# Write a function transpose() that accepts a 2D integer array matrix and returns the transpose of matrix. The transpose of a matrix is the matrix flipped over its main diagonal, swapping the rows and columns.

# 3x3 matrix before and after being transposed

# def transpose(matrix):
#     pass
# Example Usage

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# transpose(matrix)

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]
# transpose(matrix)
# Example Output:

# [
#     [1, 4, 7],
#     [2, 5, 8],
#     [3, 6, 9]
# ]
# [
#     [1, 4],
#     [2, 5],
#     [3, 6]
# ]