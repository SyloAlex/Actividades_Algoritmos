# Ejercicio 2.11: Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o
# impar.


class Numbers:
    '''
    Recibe el numero del terminal y verifica que el input sea un numero
    y no un string
    '''
    def __init__(self):
        self.number = 0
    
    def get_input(self):
        valid = False
        while not valid:
            try:
                inp = input("Ingrese un numero: ")
                self.number = int(inp)
                valid = True
            except ValueError:
                print("Las letras no son numeros :/ Por favor escriba un numero")

    def check_odd_even(self):
        '''
        Revisa si el numero ingresado en el terminal es positivo o negativo y par o 
        impar, e imprime el resultado de la verificacion
        '''
        self.get_input()
        if self.number > 0:
            if self.number % 2 == 0:
                print(f"El numero {self.number} es un numero par y positivo")
            else:
                print(f"El numero {self.number} es un numero impar y positivo")
        if self.number < 0:
            if self.number % 2 == 0:
                print(f"El numero {self.number} es un numero par y negativo")
            else:
                print(f"El numero {self.number} es un numero impar y negativo")
        if self.number == 0:
            print(f"El numero {self.number} es tecnicamente considerado par")

data = Numbers().check_odd_even()