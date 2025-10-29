# from sum_list_cython import sum_integers_in_list

# python_numbers = [i for i in range(1, 1000001)]
# result = sum_integers_in_list(python_numbers)
# print(result)

import numpy as np
import matrix_multiply

A = [[i for i in range(1,100)], [i for i in range(100,200)]]
B = [[i for i in range(200,300)], [i for i in range(300,400)]]

result = matrix_multiply.multiply_matrices(A, B)
print(result)