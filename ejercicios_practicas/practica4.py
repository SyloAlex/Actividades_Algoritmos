#Ejercicios de practica para la clase de Condicionales y funciones built-in de Python

from datetime import datetime

# Ejercicio 1: Dado una cadena de caracteres que represente la temperatura de la sala,
# y otra que represente la unidad de temperatura, realice un programa que convierta la
# temperatura en grados Celsius y lo imprima.

class Thermometer:

    def __init__(self):
        self.temperature = 0
        self.unit = ""
    
    def get_input(self):
        '''
            Obtiene del usuario la temperatura y su unidad de medida
        '''
        valid = False
        while valid is False:
            try:
                unit = input("Escribe la unidad de medida (F o K): ")
                if unit.isalpha() and (unit == "F" or unit == "K"):
                    self.unit = unit
                    temperature = input("Escribe la temperatura actual de la sala: ")
                    self.temperature = float(temperature)
                    valid = True
                else:
                    print("La unidad seleccionada no corresponde a las opciones")
            except ValueError:
                print("La temperatura indicada no es un numero")

    def transform_to_celsius(self):
        print("Bienvenido a tu termometro!")
        self.get_input()
        if self.unit == "K":
            celsius = self.temperature - 273.15
        else:
            celsius = (self.temperature - 32)*(5/9)
        print(f"La temperatura {self.temperature}{self.unit} en celsius es {celsius}C.")


# termometro = Thermometer().transform_to_celsius()

# Ejercicio 2: Realice un programa que le pida al usuario Nombre, Apellido y Edad.
# Imprima la cantidad de letras en nombre y apellido, y dos posibles años de nacimiento.
# Si el nombre tiene mas de 6 caracteres, imprimir:

class ClientData:
    '''
        Obtiene el nombre, apellido y edad del usuario para imprimir la cantidad de caracteres
        y posibles años de nacimiento
    '''
    def __init__(self):
        self.name = ""
        self.last_name = ""
        self.age = 0
    
    def get_input(self):
        '''
            Obtiene del usuario su nombre, apellido y edad
        '''
        valid = False
        while valid is False:
            try:
                name = input("Escribe tu nombre: ")
                if name.isalpha():
                    self.name = name
                    last_name = input("Escribe tu apellido: ")
                    if last_name.isalpha():
                        self.last_name = last_name
                        age = int(input("Escribe tu edad: "))
                        self.age = age
                        valid = True
                    else:
                        print("Los apellidos no tienen numeros :/")
                else:
                    print("Los nombres no tienen numeros :(")
            except ValueError:
                print("Por favor ingresa tu edad en numeros, no letras")
    
    def print_len_data(self):
        '''
            Imprime la cantidad de letras en el nombre y apellido y
            dos posibles fechas de nacimiento
        '''
        self.get_input()
        print(f"El nombre {self.name} tiene {len(self.name)} letras")
        if len(self.name) > 6:
            print("Dude, tu nombre tiene muchos caracteres!")
        print(f"El apellido {self.last_name} tiene {len(self.last_name)} letras")
        year = datetime.today().year
        birthdate = year - self.age
        print(f"Naciste en {birthdate} o en {birthdate - 1}!")

# client = ClientData().print_len_data()

#Ejercicio 3: Descuento navideño en una tienda :)

class DiscountPrice:
    '''
        Recibe el precio del producto a comprar e imprime el descuento a aplicar
        y el nuevo precio
    '''
    def __init__(self):
        self.price = 0
    
    def get_input(self):
        '''
            Obtiene del usuario la temperatura y su unidad de medida
        '''
        valid = False
        while valid is False:
            try:
                price = float(input("Escribe el precio del producto: "))
                if price < 0:
                    print("El precio no puede ser menor a 0")
                else:
                    self.price = price
                    valid = True
            except ValueError:
                print("El precio debe estar reflejado en numero, sin letras")
    
    def get_discount(self):
        '''
            Le indica al usuario cuanto es el descuento y el precio luego de 
            aplicarlo
        '''
        self.get_input()
        if self.price >= 0 and self.price < 800:
            print("El producto no aplica para los descuentos")
        elif self.price < 1500:
            discount = "10%"
            discount_price = self.price * 0.9
        elif self.price < 5000:
            discount = "15%"
            discount_price = self.price * 0.85
        else:
            discount = "20%"
            discount_price = self.price * 0.8
        if self.price >= 800:
            print(f"El descuento aplicado es de {discount}, el precio con el descuento es de {discount_price}$")

# cat = DiscountPrice().get_discount()