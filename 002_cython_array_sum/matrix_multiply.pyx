import cython
def multiply_matrices(list matrix_a, list matrix_b):
    cdef int n = len(matrix_a)
    cdef int i, j, k
    cdef list result = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]
    return result