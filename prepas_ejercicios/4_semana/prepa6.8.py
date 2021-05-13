# Escribir un programa que cree un diccionario simulando una cesta de la compra. 
# El programa debe preguntar el artículo y su precio y añadir el par al diccionario, 
# hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra 
# y el coste total, con el siguiente formato:

class ShoppingCart:
    '''
        Carrito de compras donde se puede almacenar item, cantidad y precio
        A su vez se puede imprimir la lista antes de finalizar el programa
    '''
    def __init__(self):
        self.cart = {}

    def get_item(self):
        '''
            El cliente ingresa el producto, cantidad a comprar y precio.
        '''
        item = input("Que articulo va a comprar?: ")
        valid = False
        while valid is False:
            try:
                quantity = int(input("Cuantos va a agregar?: "))
                price = float(input("Cual es el precio?: "))
                valid = True
            except ValueError:
                print("Debe ingresar un numero")
        return item, quantity, price

    def add_items_to_cart(self, item, quantity, price):
        '''
            Añade al carrito los datos del producto. Item = nombre del producto
            quantity = cantidad en enteros, price = precio en floats
        '''
        self.cart[item] = {}
        self.cart[item]["Cantidad"] = quantity
        self.cart[item]["Precio"] = price

    def print_cart(self):
        '''
            Imprime el carrito de compras con todos los productos ingresados
        '''
        print("Lista de compras")
        price = 0
        for items, values in self.cart.items():
            print("{} >>> Cantidad: {} Precio: {}$ Total: {}$".format(items.capitalize(), 
                                                          values.get("Cantidad"), 
                                                          values.get("Precio"),
                                                          values.get("Cantidad") * values.get("Precio")))
            price += values.get("Cantidad") * values.get("Precio")
        print(f"Total de la compra: {price}$")

    def execute(self):
        '''
            Ejecuta las funciones get_item(), add_items_to_cart() y 
            print_cart()
        '''
        valid = False
        print("Bienvenido a su carrito de compras virtual")
        while valid is False:
            item, quantity, price = self.get_item()
            self.add_items_to_cart(item, quantity, price)
            option = input("Desea agregar otro producto? (Si o No): ")
            if option.lower() == "no":
                print_option = input("Desea imprimir su carrito de compras? (Si o No): ")
                if print_option.lower() == "no":
                    print("Entendido, que tenga un feliz dia")
                    valid = True
                elif print_option.lower() == "si":
                    print("\n--------------------------")
                    self.print_cart()
                    valid =True

ShoppingCart().execute()