# Ejercicio 3.13: Realice un algoritmo que dado un número N cualquiera, encuentre dos números
# primos A y B que al ser multiplicados resulte el número N. De no existir ningunos números
# A y B que cumplan la condición, el algoritmo deberá imprimir un mensaje de error

def get_input():
    '''
    Recibe el numero
    '''
    valid = False
    while not valid:
        try:
            inp = input("Por favor, ingrese el numero: ")
            inp_number = int(inp)
            valid = True
        except ValueError:
            print("Las letras no son numeros :/ Por favor escriba un numeros")
    return inp_number

def find_prime_numbers(number):
    '''
        Busca los numeros primos que componen el input y revisa si la multiplicacion de
        algunos da como resultado el input
    '''
    prime_numbers = []
    prime_combination = []
    for n in range(2, number):
        if number % n == 0:
            prime_numbers.append(n)
    if prime_numbers == []:
        print("Este numero es un numero primo.\nNo hay numeros divisibles que den como resultado es numero")
    else:
        for prime in prime_numbers:
            for prime2 in prime_numbers:
                if prime * prime2 == number:
                    if [prime2, prime] not in prime_combination:
                        prime_combination.append([prime, prime2])
        if prime_combination == 0:
            print("No hay numeros primos que den como resultado el numero ingresado")
        else:
            print(f"El reultado es: {prime_combination}")

numero = get_input()
find_prime_numbers(numero)