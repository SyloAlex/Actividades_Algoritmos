# Ejercicio 3.9: Elabore un algoritmo que imprima por pantalla los 10 primeros números de la
# sucesión Fibonacci.


def print_fibonacci():
    '''
        Calcula la sucesion de fibonacci y la imprime
    '''
    n = 1
    fibonacci_number = 1
    stepper = 1
    fibonacci = [0, 1, 1]
    for num in range(1, 8):
        stepper = fibonacci_number
        fibonacci_number += n
        fibonacci.append(fibonacci_number)
        n = stepper
    print(fibonacci)

print_fibonacci()