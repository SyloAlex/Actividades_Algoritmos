# Ejercicio 3.1: Realiza un programa que, dado un número entero positivo ingresado por teclado,
# imprima la suma de los números que lo componen. Si el valor de la suma es menor 
# que 10, la respuesta es el valor obtenido, si no, es la suma de los dígitos de 
# la suma de los dígitos

def get_input():
    '''
        Obtiene del usuario el numero para realizar el calculo
        matematico
    '''
    valid = False
    while valid is False:
        number = input("Por favor, escriba el numero: ")
        if number.isnumeric():
            valid = True
        else:
            print("La opcion seleccionada no es un numero")
    return number

def get_digit_sum(input):
    result = 0
    for digit in input:
        result += int(digit)
        if result >= 10:
            new_result = str(result)
            result = 0
            for digit in new_result:
                result += int(digit)
    return result

def execute():
    print("Bienvenido a la funcion suma de digitos!")
    number_input = get_input()
    output = get_digit_sum(number_input)
    print("El resultado obtenido es:", output)

execute()