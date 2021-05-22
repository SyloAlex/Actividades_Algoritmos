# Ejercicio 1: Realice una funcion que permita calcular la combinatoria:
# n!/(k!)(n-k)!

def calculate_factorial(number):
    '''
        Calcula el factorial del numero ingresado. 
        
        Arguments:
        Number = {int}.

        Returns:
        result = {int}
    '''
    result = 1
    if number > 1:
        for num in range(1, number + 1):
            result *= num
    elif number == 0 or number == 1:
        result = 1
    else:
        raise ValueError
    
    return result

def calculate_ecuation(num1, num2):
    """
        Calcula la combinatoria de n en k.

        Argument:
        num1, num2 = {int}

        Return:
        factorial_result = {float}
    """
    if num1 < 0 or num2 < 0 or num1-num2 < 0:
        factorial_result = "No se puede calcular el factorial de un numero negativo"
    else:
        factorial_result = calculate_factorial(num1) / (calculate_factorial(num2) * calculate_factorial(num1-num2))
    
    return factorial_result

# Ejercicio 2: Realice una funcion que reciba un parametro desconocido y otra funcion como parametro
# (el default sera la funcion print) y que le aplique esta funcion al parametro

def new_function(param, function= print):
    function(param)

# Main de los ejercicios practicos

def main():
    '''
        Ejecuta los 2 ejercicios practicos
    '''
    n = 7
    k = 3
    combinatory_result = calculate_ecuation(n,k)
    print("El resultado es", combinatory_result)
    param = "Hola Mundo!"
    new_function(param)

if __name__ == "__main__":
    main()