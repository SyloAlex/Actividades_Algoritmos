# Escribe un programa que, dado un número n, imprima la sucesión de Fibonacci, separada por comas, 
# hasta el número igual o más cercano que haya por debajo de n

def get_input():
    '''
    Recibe el numero para imprimir la serie de Fibonacci
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
        Calcula la sucesion de fibonacci y la imprime
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
    fibonacci.pop(-1)
    print(fibonacci)

numero = get_input()
print_fibonacci(numero)