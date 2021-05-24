# Ejercicio 5.7: Realice un algoritmo que calcule la factorial de un número.

def get_input():
    '''
        Obtiene del usuario el numero para calcular el factorial

        Input:
        number = {int+}
    '''
    valid = False
    while valid is False:
        try:
            number = int(input("Por favor, ingrese el numero:\n>> "))
            if number >= 0:
                valid = True
            else:
                print("Los numeros negativos no tienen factorial")
        except ValueError:
            print("No ingresaste un numero")
    
    return number

def factorial(number):
    '''Calculo de factorial

    Arguments:
    number = {int}

    Returns:
    result = factorial de number {int}
    '''
    if number == 0 or number == 1:
        print(f"El factorial de {number} es 1!")
    else:
        result = 1
        for numbers in range(1, number + 1):
            result *= numbers
    
    return result

def main():
    number = get_input()
    result = factorial(number)
    print(f"El factorial de {number} es {result}!")

main()