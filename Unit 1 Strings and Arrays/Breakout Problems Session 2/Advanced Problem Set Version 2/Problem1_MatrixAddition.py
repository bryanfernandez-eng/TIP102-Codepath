# Write a function add_matrices() that accepts to n x m matrices matrix1 and matrix2. The function should return an n x m matrix sum_matrix that is the sum of the given matrices such that each value in sum_matrix is the sum of values of corresponding elements in matrix1 and matrix2.

# def add_matrices(matrix1, matrix2):
#     pass
# Example Usage

# matrix1 = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# matrix2 = [
#     [9, 8, 7],
#     [6, 5, 4],
#     [3, 2, 1]
# ]

# add_matrices(matrix1, matrix2)
# Example Output:

# [
#     [10, 10, 10],
#     [10, 10, 10],
#     [10, 10, 10]
# ]


def add_matrices(matrix1, matrix2):
    sum_matrix = [[0 for _ in range(len(matrix1[0]))] for _ in range(len(matrix1))]

    for row in range(len(matrix1)): 
        for col in range(len(matrix1[0])): 
            sum_matrix[row][col] = matrix1[row][col] + matrix2[row][col]
    print(sum_matrix)
    return sum_matrix

matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

add_matrices(matrix1, matrix2)