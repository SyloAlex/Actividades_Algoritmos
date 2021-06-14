# Realiza un programa que, dado un número entero positivo ingresado por 
# teclado, imprima la suma de los números que lo componen. Si el valor de 
# la suma es menor que 10, la respuesta es el valor obtenido, si no, es la 
# suma de los dígitos de la suma de los dígitos. Por ejemplo: para 7 es 7, 
# para 12 es 3, y para 845 es 8 (8+4+5 = 17 => 1+7 = 8)

def get_number():
    while True:
        try:
            number = int(input("Ingrese un numero:\n>> "))
            if len(str(number)) > 0:
                break
            else:
                print("Ingrese un numero entero positivo")
        except:
            print("Por favor solo ingrese numeros")
    
    return number

def sum_digits(number):
    if len(str(number)) == 1:
        return number
    else:
        result = int(str(number)[0]) + sum_digits(int(str(number)[1:]))
        if result > 10:
            return sum_digits(result)
        else:
            return result

print(sum_digits(get_number()))