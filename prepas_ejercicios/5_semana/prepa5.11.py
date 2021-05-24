# Ejercicio 5.11: Escribir una función que reciba una muestra de números en una lista y 
# devuelva otra lista con sus cuadrados.

def get_list():
    '''
        Obtiene del usuario una lista de numeros.

        Input >> {int}
    '''
    result = []
    while True:
        try:
            lenght = int(input("Ingrese el tamano de la lista\n>> "))
            break
        except ValueError:
            print("Error: no introduzca letras o caracteres especiales")
    while True:
        try:
            for num in range(lenght):
                num_for_list = int(input(f"Ingrese el numero en la posicion {num}\n>> "))
                result.append(num_for_list)
            break
        except ValueError:
            print("Error: no introduzca letras o caracteres especiales")
    
    return result

def square_list(list_num):
    '''Cuadrado de numeros

    Arguments:
    list_num = lista de numeros {list}

    Returns:
    result = cuadrado de cada numero en la lista {list}
    '''
    result = [x**2 for x in list_num]
    
    return result

list_of_numbers = get_list()
result = square_list(list_of_numbers)
print(result)