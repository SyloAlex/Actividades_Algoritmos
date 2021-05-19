# Ejercicio 3.6: Diseña un programa que permita realizar las siguientes operaciones matemáticas: Suma,
# Resta, Multiplicación, División, Potencia.

class Calculator:
    '''
        Calculadora capaz de realizar sumas, restas, divisiones, multiplicaciones, 
        modulo, valor absoluto, comparacion entre dos numero y potencia.
    '''
    def __init__(self):
        self.number1 = 0
        self.number2 = 0
        self.compare = ""
    
    def get_input(self):
        '''
            Obtiene del usuario la opcion para realizar el calculo
            matematico
        '''
        print("1.Suma\n2.Resta\n3.Multiplicacion\n4.Division\n5.Potencia")
        valid = False
        while valid is False:
            try:
                option = input("Por favor, indiquenos la opcion:\n>> ")
                option = int(option)
                if option >= 1 and option <= 5:
                    valid = True
                else:
                    print("La opcion seleccionada no es valida")
            except ValueError:
                print("La opcion que seleccionaste no es un numero")
        
        return option

    def sum_subs_multi_numbers(self, option):
        '''
            Obtiene del usuario los numeros para realizar la suma, resta o multiplicacion
        '''
        valid = False
        while valid is False:
            try:
                self.number1 = int(input("Ingrese el primer numero:\n>> "))
                self.number2 = int(input("Ingrese el segundo numero:\n>> "))
                valid = True
            except ValueError:
                print("Por favor, ingrese los numeros con los que desea hacer la operacion")
        if option == 1:
            result = self.number1 + self.number2
        elif option == 2:
            result = self.number1 - self.number2
        else:
            result = self.number1 * self.number2
        
        return result

    def divide_numbers(self):
        '''
            Obtiene del usuario los numeros para realizar la division
        '''
        print("Division de numeros")
        valid = False
        while valid is False:
            try:
                self.number1 = int(input("Ingrese el dividendo numero:\n>> "))
                number2 = int(input("Ingrese el divisor numero:\n>> "))
                if number2 == 0:
                    print("No se puede dividir entre cero")
                else:
                    valid = True
                    self.number2 = number2
            except ValueError:
                print("Por favor, ingrese los numeros con los que desea hacer la operacion")
        result = self.number1 / self.number2
        
        return result

    def exponential_numbers(self):
        '''
            Obtiene del usuario los numeros para realizar la potencia
        '''
        print("Exponencial")
        valid = False
        while valid is False:
            try:
                self.number1 = int(input("Ingrese el numero base:\n>> "))
                self.number2 = int(input("Ingrese la potenciao:\n>> "))
                valid = True
            except ValueError:
                print("Por favor, ingrese los numeros con los que desea hacer la operacion")
        result = self.number1 ** self.number2
        
        return result

    def calculate(self):
        print("Bienvenido!!")
        valid = False
        while valid is False:
            option = self.get_input()
            if option >= 1 and option <= 3:
                result = self.sum_subs_multi_numbers(option)
            elif option == 4:
                result = self.divide_numbers()
            else:
                result = self.exponential_numbers()
            print("El resultado es:", result)
            valid_calculate = False
            while valid_calculate is False:
                try:
                    check = input("Desea realizar otra operacion:\nSi\nNo:\n>> ").lower()
                    if check.isalpha() is True and check == "no":
                        print("Entendido, espero tenga un feliz dia")
                        valid_calculate = True
                        valid = True
                    if check.isalpha() is True and check == "si":
                        print("Perfecto")
                        valid_calculate = True
                except ValueError:
                    print("La opcion seleccionada no es valida")

calculator = Calculator().calculate()