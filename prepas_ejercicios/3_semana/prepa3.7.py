# Ejercicio 3.7: Realice un algoritmo que calcule la factorial de un número.

def get_input():
    '''
        Obtiene del usuario el numero para calcular el factorial
    '''
    valid = False
    while valid is False:
        try:
            number = int(input("Por favor, ingrese el numero:\n>> "))
            valid = True
        except ValueError:
            print("No ingresaste un numero")
    
    return number

def factorial(number):
    if number == 0 or number == 1:
        print(f"El factorial de {number} es 1!")
    else:
        result = 1
        for numbers in range(1, number + 1):
            result *= numbers
        print(f"El factorial de {number} es {result}!")

number = get_input()
factorial(number)