# Escribir un programa que guarde en un diccionario los precios de las frutas de 
# la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por 
# pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario 
# debe mostrar un mensaje informando de ello.

class Fruit_Store:
    def __init__(self):
        self.database = {"Uva": 1.35, "Manzana": 1, "Pera": 0.85, "Naranja": 0.75}
    
    def get_input(self):
        fruit = input("\nIngrese la fruta que desea comprar:\n>> ").capitalize()
        if fruit in self.database:
            valid = False
            while valid is False:
                try:
                    quantity = int(input("Cuantas frutas desea?:\n>> "))
                    valid = True
                except ValueError:
                    print("Por Favor escriba la cantidad solo con numeros")
        else:
            print("No tenemos ese producto en nuestro almacen")

        return fruit, quantity

    def check_price(self, fruit_name, fruit_quantity):
        for fruit, price in self.database.items():
            if fruit == fruit_name:
                fruit_price = price * fruit_quantity

        return fruit_price

    def print_database(self):
        print("Este es nuestro menu!")
        for fruit, price in self.database.items():
            print("-------------\nFruta: {}\nPrecio: {}".format(fruit, price))

    def execute(self):
        print("Bienvenidos a la Fruteria 'Sin Mango'!")
        self.print_database()
        valid = False
        while valid is False:
            fruit, quantity = self.get_input()
            price = self.check_price(fruit, quantity)
            print("La compra de {} {} da un total de {}$".format(quantity, fruit, price))
            continue_shopping = input("Desea continuar con su compra?:\n>> ")
            continue_valid = False
            while continue_valid is False:
                if continue_shopping == "si":
                    continue_valid = True
                    continue
                elif continue_shopping == "no":
                    continue_valid = True
                    valid = True
                    print("Entendido, que tenga un feliz dia!")
                else:
                    print("Esa opcion no es valida")

Fruit_Store().execute()
