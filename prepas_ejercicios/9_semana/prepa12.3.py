# Realice un algoritmo que calcule el factorial de un número.

def get_number():
    while True:
        try:
            number = int(input("Ingrese un numero:\n>> "))
            if len(str(number)) >= 0:
                break
            else:
                print("Ingrese un numero entero positivo")
        except:
            print("Por favor solo ingrese numeros")
    
    return number

def number_factorial(number):
    if number == 1 or number == 0:
        return 1
    result = number * number_factorial(number - 1)
    
    return result

print(number_factorial(get_number()))