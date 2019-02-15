"""
Compute the matrix multiplication of two matricies.
If matrix A is n x m and matrix B is m x p, then resulting matrix C is n x p
C(i,j) = A(i,1)*B(1,j) + ... + A(i,m)*B(m,j)
where i = 1...n and j = 1...p
"""
__author__ = "Gary Tang"


def dot_product(vec1, vec2):
    """
    @param vec1: List[List[int]]
    @param vec2: List[List[int]]
    """
    v1_row, v1_col = len(vec1), len(vec1[0])
    v2_row, v2_col = len(vec2), len(vec2[0])
    if v1_col != v2_row:
        return -1

    # init matrix
    matrix = [[0 for col in range(v2_col)] for row in range(v1_row)]
    for row in range(v1_row):
        for col in range(v2_col):
            for inner in range(v1_row):
                matrix[row][col] += vec1[row][inner]*vec2[inner][col]

    return matrix


vec1 = [[1,2], [3,4]]
vec2 = [[7,8], [9,10]]
print(dot_product(vec1, vec2))
