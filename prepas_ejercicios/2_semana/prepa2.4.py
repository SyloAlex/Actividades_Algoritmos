# Diseña un programa que permita realizar las siguientes operaciones matemáticas: Suma,
# Resta, Multiplicación, División, Potencia, Módulo, Comparar (mayor o menor que), Valor absoluto

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
        print("1.Suma\n2.Resta\n3.Multiplicacion\n4.Division\n5.Potencia\n6.Modulo\n7.Comparar dos numeros\n8.Valor Absoluto")
        valid = False
        while valid is False:
            try:
                option = input("Por favor, indiquenos la opcion: ")
                option = int(option)
                if option >= 1 and option <= 8:
                    valid = True
                else:
                    print("La opcion seleccionada no es valida")
            except ValueError:
                print("La opcion que seleccionaste no es un numero")
        return option
    
    def sum_numbers(self):
        '''
            Obtiene del usuario los numeros para realizar la suma
        '''
        print("Suma de numeros")
        valid = False
        while valid is False:
            try:
                self.number1 = int(input("Ingrese el primer numero: "))
                self.number2 = int(input("Ingrese el segundo numero: "))
                valid = True
            except ValueError:
                print("Por favor, ingrese los numeros con los que desea hacer la operacion")
        result = self.number1 + self.number2
        print("El resultado es:", result)

    def substract_numbers(self):
        '''
            Obtiene del usuario los numeros para realizar la resta
        '''
        print("Resta de numeros")
        valid = False
        while valid is False:
            try:
                self.number1 = int(input("Ingrese el primer numero: "))
                self.number2 = int(input("Ingrese el segundo numero: "))
                valid = True
            except ValueError:
                print("Por favor, ingrese los numeros con los que desea hacer la operacion")
        result = self.number1 - self.number2
        print("El resultado es:", result)

    def multiply_numbers(self):
        '''
            Obtiene del usuario los numeros para realizar la multiplicacion
        '''
        print("Multiplicacion de numeros")
        valid = False
        while valid is False:
            try:
                self.number1 = int(input("Ingrese el primer numero: "))
                self.number2 = int(input("Ingrese el segundo numero: "))
                valid = True
            except ValueError:
                print("Por favor, ingrese los numeros con los que desea hacer la operacion")
        result = self.number1 * self.number2
        print("El resultado es:", result)

    def divide_numbers(self):
        '''
            Obtiene del usuario los numeros para realizar la division
        '''
        print("Division de numeros")
        valid = False
        while valid is False:
            try:
                self.number1 = int(input("Ingrese el dividendo numero: "))
                number2 = int(input("Ingrese el divisor numero: "))
                if number2 == 0:
                    print("No se puede dividir entre cero")
                else:
                    valid = True
                    self.number2 = number2
            except ValueError:
                print("Por favor, ingrese los numeros con los que desea hacer la operacion")
        result = self.number1 / self.number2
        print("El resultado es:", result)

    def exponential_numbers(self):
        '''
            Obtiene del usuario los numeros para realizar la potencia
        '''
        print("Exponencial")
        valid = False
        while valid is False:
            try:
                self.number1 = int(input("Ingrese el numero base: "))
                self.number2 = int(input("Ingrese la potenciao: "))
                valid = True
            except ValueError:
                print("Por favor, ingrese los numeros con los que desea hacer la operacion")
        result = self.number1 ** self.number2
        print("El resultado es:", result)

    def module_numbers(self):
        '''
            Obtiene del usuario los numeros para realizar el modulo
        '''
        print("Modulo de dos numeros")
        valid = False
        while valid is False:
            try:
                self.number1 = int(input("Ingrese el dividendo numero: "))
                number2 = int(input("Ingrese el divisor numero: "))
                if number2 == 0:
                    print("No se puede dividir entre cero")
                else:
                    valid = True
                    self.number2 = number2
            except ValueError:
                print("Por favor, ingrese los numeros con los que desea hacer la operacion")
        result = self.number1 % self.number2
        print("El resultado es:", result)
    
    def compare_numbers(self):
        '''
            Obtiene del usuario los numeros para realizar una comparacion entre dos numeros
        '''
        print("Comparacion entre dos numeros")
        valid = False
        while valid is False:
            try:
                self.number1 = int(input("Ingrese el primer numero: "))
                self.number2 = int(input("Ingrese el segundo numero: "))
                valid = True
            except ValueError:
                print("Por favor, ingrese los numeros con los que desea hacer la operacion")
        valid = False
        while valid is False:
            try:
                comparison = input("Ingrese la opcion <, >, <=, >=, = o !=: ")
                if comparison == "<":
                    result = self.number1 < self.number2
                    valid = True
                elif comparison == ">":
                    result = self.number1 > self.number2
                    valid = True
                elif comparison == "<=":
                    result = self.number1 <= self.number2
                    valid = True
                elif comparison == ">=":
                    result = self.number1 >= self.number2
                    valid = True
                elif comparison == "=":
                    result = self.number1 == self.number2
                    valid = True
                elif comparison == "!=":
                    result = self.number1 != self.number2
                    valid = True
                else:
                    raise ValueError
            except ValueError:
                print("La opcion que seleccionaste no es valida")
        print("El resultado de", self.number1, comparison, self.number2, "es:", result)

    def absolute_value(self):
        '''
            Obtiene del usuario el numero para calcular el valor absoluto
        '''
        print("Valor absoluto de un numero")
        valid = False
        while valid is False:
            try:
                self.number1 = int(input("Ingrese el numero: "))
                if self.number1 >= 0:
                    result = self.number1
                    valid = True
                if self.number1 < 0:
                    result = self.number1 * -1
                    valid = True
            except ValueError:
                print("Por favor, ingrese los numeros con los que desea hacer la operacion")
        print("El resultado es:", result)

    def calculate(self):
        print("Bienvenido!!")
        valid = False
        while valid is False:
            option = self.get_input()
            if option == 1:
                self.sum_numbers()
            elif option == 2:
                self.substract_numbers()
            elif option == 3:
                self.multiply_numbers()
            elif option == 4:
                self.divide_numbers()
            elif option == 5:
                self.exponential_numbers()
            elif option == 6:
                self.module_numbers()
            elif option == 7:
                self.compare_numbers()
            else:
                self.absolute_value()
            valid_calculate = False
            while valid_calculate is False:
                try:
                    check = input("Desea realizar otra operacion:\nSi\nNo:\n")
                    if check.isalpha() is True and check == "No":
                        print("Entendido, espero tenga un feliz dia")
                        valid_calculate = True
                        valid = True
                    if check.isalpha() is True and check == "Si":
                        print("Perfecto")
                        valid_calculate = True
                except ValueError:
                    print("La opcion seleccionada no es valida")

calculator = Calculator().calculate()