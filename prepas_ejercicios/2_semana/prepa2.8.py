# Ejercicio 2.8: Elabore un programa que se encargue de solicitar 3 números que serán el día, mes y año de una fecha. 
# El programa debe indicar si la fecha es correcta y leerla por consola.

class Date:
    '''
    Recibe la fecha del terminal y verifica que el input sea un numero valido
    '''
    def __init__(self):
        self.month = 12
        self.day = None
        self.year = None

    def get_month(self):
        '''
        Recibe el mes del terminal y verifica que el input sea un numero valido
        '''
        valid = False
        while not valid:
            try:
                inp = input("Por favor, ingrese el numero del mes: ")
                self.month = int(inp)
                if self.month <= 0 or self.month > 12:
                    print("No es posible anexar este mes a la fecha")
                else:
                    valid = True
            except ValueError:
                print("Las letras no son numeros :/ Por favor escriba el mes en numeros")

    def get_year(self):
        '''
        Recibe el año del terminal y verifica que el input sea un numero valido
        '''
        valid = False
        while not valid:
            try:
                inp = input("Por favor, ingrese el año: ")
                self.year = int(inp)
                if self.year <= 0:
                    print("No es posible anexar este año a la fecha")
                else:
                    valid = True
            except ValueError:
                print("Las letras no son numeros :/ Por favor escriba el año en numeros")

    def get_day(self):
                '''
        Recibe el dia del terminal y verifica que el input sea un numero valido
        '''
        valid = False
        while not valid:
            try:
                inp = input("Por favor, ingrese el dia: ")
                self.day = int(inp)
                if self.month == 1 or self.month == 3 or self.month == 5 or self.month == 7 or self.month == 8 or self.month == 10 or self.month == 12:
                    if self.day > 31:
                        print("El mes seleccionado no puede tener mas de 31 dias")
                    elif self.day <= 0:
                        print("No pueden haber dias negativos o igual a 0")
                    else:
                        valid = True
                if self.month == 4 or self.month == 6 or self.month == 9 or self.month == 11:
                    if self.day > 30:
                        print("El mes seleccionado no puede tener mas de 30 dias")
                    elif self.day <= 0:
                        print("No pueden haber dias negativos o igual a 0")
                    else:
                        valid = True
                if self.month == 2:
                    if self.day > 28:
                        print("El mes seleccionado no puede tener mas de 28 dias")
                    elif self.day <= 0:
                        print("No pueden haber dias negativos o igual a 0")
                    else:
                        valid = True
            except ValueError:
                print("Las letras no son numeros :/ Por favor escriba el dia en numeros")
    
    def execute_dates(self):
        '''
            Ejecuta las funciones necesarias para imprimir la fecha obtenida del usuario
        '''
        self.get_month()
        self.get_day()
        self.get_year()
        print("La fecha seleccionada fue:", str(self.day) + "/" + str(self.month) + "/" + str(self.year))

date = Date().execute_dates()