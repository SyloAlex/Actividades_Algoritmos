# Realice un algoritmo que dado un número ingresado por un usuario realice la
# operación de multiplicación por la matriz A del ejercicio anterior, el programa deberá
# mostrar como respuesta la matriz resultante de la misma

import numpy as np

matrix1 = [[1, 4, 6],
           [4, 2, 5],
           [6, 5, 3]]

def get_input():
    '''
    Recibe el numero
    '''
    valid = False
    while not valid:
        try:
            inp = input("Por favor, ingrese el numero: ")
            inp_number = int(inp)
            valid = True
        except ValueError:
            print("Las letras no son numeros :/ Por favor escriba un numeros")
    return inp_number

#test = get_input()
def mult_matrix(number, matrix):
    mult_matrix = np.multiply(matrix, number)
    print(mult_matrix)

test = get_input()
mult_matrix(test, matrix1)