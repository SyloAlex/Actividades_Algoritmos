# Ejercicio 3.10: Dado un entero X de tres dígitos diferentes, 
# imprima "SÍ" si sus tres dígitos van en orden ascendente de 
# izquierda a derecha e imprima "NO" de lo contrario.

def get_input():
    '''
        Obtiene del usuario un numero de 3 digitos
    '''
    valid = False
    while valid is False:
        number = input("Por favor, ingrese un numero de tres digitos:\n>> ")
        if number.isnumeric():
            if len(number) == 3:
                valid = True
            else:
                print("El numero ingresado no tiene 3 digitos")
        else:
            print("No ingresaste un numero")
    
    return number

def check_incremental_number(num):
    if (int(num[0]) < int(num[1])) and (int(num[1]) < int(num[2])) and (int(num[0]) < int(num[2])):
        print(f"El numero {num} tiene digitos incrementales!")
    else:
        print(f"El numero {num} no tiene digitos incrementales")

number = get_input()
check_incremental_number(number)