# Se le llama “número de dígitos incrementales” a aquel número para el que cada uno de sus dígitos 
# es menor o igual al que le sigue. Por ejemplo, 1338 es un número de dígitos incrementales; porque 
# 1<3, 3=3 y 3<8. Por otro lado, 597 no lo es; porque 5<9 pero 9>7.
# Diseña un programa que, tomando un número de dos o más dígitos por teclado, verifique si se trata 
# de un número de dígitos incrementales o no.

def get_number():
    while True:
        try:
            number = str(int(input("Ingrese un numero:\n>> ")))
            if len(str(number)) >= 2:
                break
            else:
                print("Ingrese un numero de dos digitos o mas")
        except:
            print("Por favor solo ingrese numeros")
    
    return number

def incremental(number):
    flag = True
    if len(number) == 1:
        return flag
    if number[0] > number[1]:
        flag = False
        return flag
    else:
        return incremental(number[1:])

def main():
    number = get_number()
    answer = incremental(number)
    if answer:
        print(f"El numero {number} es incremental!")
    else:
        print(f"El numero {number} NO es incremental!")
    
main()
