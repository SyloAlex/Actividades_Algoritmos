# Escribir una funcion recursiva que devuelva la serie de 
# Fibonacci hasta el numero que se le pone como limite.

def fibonacci(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)

print(fibonacci(2))