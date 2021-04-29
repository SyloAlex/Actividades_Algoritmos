#Ejercicio 2: Vaina del cine
class DataCollector:
    '''
    Recibe los datos del cliente (nombre y edad) ingresados en la terminal y verifica la factibilidad
    de lo escrito.
    '''
    def __init__(self):
        self.name = ""
        self.age = 0
    
    def get_input(self):
        self.name = input("Ingrese su nombre aqui: ")
        checker = False
        while checker is False:
            try:
                inp = input("Ingrese su edad: ")
                age = int(inp)
                if age < 0:
                    print("No puede tener una edad negativa.")
                    continue
                if age > 117:
                    print("Actualmente, la persona mas longeva del mundo tiene 117 años.", 
                          "Este edad no es factible")
                    continue
                checker = True
                self.age = age
            except ValueError:
                print("Las letras no son numeros :/ Por favor escriba su edad en numeros")
                continue

    def get_ticket_price(self):
        '''
        Segun la edad ingresada en el terminal, la funcion revisa cual es el precio adecuado
        para la entrada de cine del cliente.
        '''
        self.get_input()
        if self.age <= 4:
            price = "gratis"
            print(f"{self.name} tiene: {self.age} años y su entrada de cine es {price}!")
        elif self.age > 4 and self.age <= 18:
            price = 1.50
            print(f"{self.name} tiene: {self.age} años y su entrada de cine cuesta: {price}$")
        elif self.age > 18 and self.age < 60:
            price = 2.00
            print(f"{self.name} tiene: {self.age} años y su entrada de cine cuesta: {price}$")
        else:
            price = 1.00
            print(f"{self.name} tiene: {self.age} años y su entrada de cine cuesta: {price}$")


data = DataCollector()
data.get_ticket_price()