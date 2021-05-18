# Ejercicio 7.2: Realiza un programa que, a partir de la 
# siguiente matriz de 3x3, retorne su determinante:

matrix_example = [[1, 3, 2], 
                  [4, 5, 7], 
                  [8, 6, 9]]


def determinant(matrix):
    sum = 0
    for y_lenght in range(len(matrix)):
        middle = 1
        for x_lenght in range(len(matrix)):
            middle *= matrix[x_lenght][y_lenght]
            y_lenght += 1
            if y_lenght == len(matrix):
                y_lenght = 0
        sum += middle
    subs = 0
    for y_lenght in range(len(matrix)-1, -1, -1):
        middle = 1
        for x_lenght in range(len(matrix)):
            middle *= matrix[x_lenght][y_lenght]
            y_lenght -= 1
            if y_lenght == -1:
                y_lenght = len(matrix)-1
        subs += middle
    det = sum - subs
    print(det)
    

determinant(matrix_example)