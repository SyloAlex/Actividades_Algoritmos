# Ejercicio 3.11: Elabore un algoritmo que dado un número introducido por el usuario te permita
# saber si ese número está o no en la sucesión Fibonacci.


def get_input():
    '''
    Recibe el numero del usuario
    '''
    valid = False
    while not valid:
        try:
            inp = input("Por favor, ingrese el numero: ")
            number = int(inp)
            valid = True
        except ValueError:
            print("Las letras no son numeros :/ Por favor escriba un numeros")
    return number
    
def print_fibonacci(number):
    '''
        Calcula la sucesion de fibonacci y revisa si el numero esta dentro
    '''
    n = 1
    fibonacci_number = 1
    stepper = 1
    if number != 0:
        if number != 1:
            fibonacci = [0, 1, 1]
            while fibonacci_number <= number:
                stepper = fibonacci_number
                fibonacci_number += n
                fibonacci.append(fibonacci_number)
                n = stepper
        else:
            fibonacci = [0, 1]
    else:
        fibonacci = [0]
    if number in fibonacci:
        print(f"EL numero {number} esta dentro de la sucesion de fibonacci")
    else:
        print(f"EL numero {number} no esta dentro de la sucesion de fibonacci")

numero = get_input()
print_fibonacci(numero)