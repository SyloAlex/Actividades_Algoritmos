# Ejercicio 5.4: Realice una función que dado un array o vector pasada por parámetro pedir un
# número al usuario y si este no está en el vector agregarlo al final del mismo, si no, imprimir
# en pantalla un mensaje que diga: “El número introducido ya está en el vector”.

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

def get_num():
    '''
        Obtiene del usuario una lista de numeros.

        Input >> {int}
    '''
    while True:
        try:
            num = int(input("Ingrese el numero a verificar\n>> "))
            break
        except ValueError:
            print("Error: no introduzca letras o caracteres especiales")
    
    return num

def check_num(num, array):
    if num in array:
        print("El numero ingresado ya esta en la lista")
    else:
        array.append(num)
        print("Se anexo el numero {} a la lista".format(num))
    
    return array

def print_array(array):
    print("Lista:")
    i = 0
    for number in array:
        print(f"Posicion {i}: {number}")
        i += 1

def main():
    array = get_list()
    number = get_num()
    array = check_num(number, array)
    print_array(array)

main()