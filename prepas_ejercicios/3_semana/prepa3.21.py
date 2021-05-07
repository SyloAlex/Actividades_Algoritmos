# Ejericio 3.21: Realice un algoritmo que realice las operaciones de suma y resta entre las siguientes
# matrices y el output del programa devuelva dos matrices, una correspondiente a cada
# operación.

import numpy as np

matrix1 = [[1, 4, 6],
           [4, 2, 5],
           [6, 5, 3]]

matrix2 = [[1.3, 20, 12],
           [1.8, 28, 15],
           [2.5, 40, 18]]

def matrix_sum(x, y):
    x = np.array(x)
    y = np.array(y)
    sum_matrix = np.add(x, y)
    print(sum_matrix)

matrix_sum(matrix1, matrix2)