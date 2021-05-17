# Ejercicio 1: Escribe un programa que reciba un arreglo bidimensional y revise si es
# simetrico.

def get_array():
    valid_lenght = False
    while not valid_lenght:
        try:
            matrix_lenght = int(input("Ingrese el tamaño de la matriz (un solo numero): "))
            valid_lenght = True
        except ValueError:
            print("Ingrese un numero, no letras o caracteres especiales")
    ext_array = []
    valid = False
    while not valid:
        try:
            for y_lenght in range(matrix_lenght):
                in_array = []
                for x_lenght in range(matrix_lenght):
                    number = int(input(f"Ingresa el valor en la posicion [{y_lenght}][{x_lenght}]: "))
                    in_array.append(number)
                ext_array.append(in_array)
            valid = True
        except ValueError:
            print("La matriz solo acepta numeros.")
    print(*ext_array, sep="\n")
    return ext_array

def check_simetry(matrix):
    flag = True
    for y_lenght in range(len(matrix)):
        for x_lenght in range(0, y_lenght + 1):
            if not matrix[y_lenght][x_lenght] == matrix[x_lenght][y_lenght]:
                flag = False
                break
        if not flag:
            break
    if flag:
        print("La matriz es simetrica")
    else:
        print("La matriz NO es simetrica")

trial = get_array()
check_simetry(trial)