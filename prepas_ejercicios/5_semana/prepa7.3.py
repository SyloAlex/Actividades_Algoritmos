# Una panadería te ha contratado para que le diseñes un programa que tome los 
# pedidos de sus clientes, a partir de la información de una base de datos dada, 
# y generes una factura de su compra. Debes asignarle a cada cliente nuevo un número de factura, 
# además de solicitar su nombre y su cédula.

class Bakery:
    '''
        Creador de Facturas de la Panaderia
    '''
    def __init__(self):
        self.database = {"Cachito": 4.00, "Empanada": 3.00, "Pastelito": 3.50, 
                         "Sandwich": 2.50, "Pan tradicional": 1.00, 
                         "Pan especial": 1.75, "Cafe": 1.25, "Jugo": 2.00, 
                         "Agua": 0.75, "Dulces": 6.00, 
                         "Galletas": 5.75, "Torta": 10.25
        }
        self.receipt = {}
        self.total = 0
        self.allreceipts = {}
    
    def get_products(self):
        '''
            Obtiene del usuario los productos y cantidad que desea comprar.
        '''
        print("Este es nuestro menu:")
        new_receipt = {}
        new_total = 0
        for food, price in self.database.items():
            print(f"{food} = {price}$")
        valid = False
        while valid is False:
            order = input("Que desea ordenar?\n>>> ").capitalize()
            if order not in self.database:
                print("No tenemos ese producto en el menu")
            else:
                try:
                    quantity = int(input("Cuantos va a ordenar?: "))
                    new_receipt[order] = {"Cantidad": quantity, "Total": self.database[order] * quantity}
                    new_total += (self.database[order] * quantity)
                    order_valid = False
                    while order_valid is False:
                        continue_order = input("Desea ordenar algo mas? (Si o No): ").lower()
                        if continue_order == "si":
                            order_valid = True
                        elif continue_order == "no":
                            order_valid = True
                            valid = True
                        else:
                            print("Esa opcion no es valida")
                except ValueError:
                    print("Introduzca la cantidad en numeros")
        return new_receipt, new_total

    def check_for_discount(self, new_total):
        '''
            Revisa si el total de la factura es multiplo de 3 o 7
            para calcular el descuento
        '''
        if (new_total % 3) == 0:
            if (new_total % 7) == 0:
                print("Por su compra tuvo un descuento del 15%!")
                new_total -= (new_total*0.15)
            else:
                print("Por su compra tuvo un descuento del 10%!")
                new_total -= (new_total*0.10)
        elif (new_total % 7) == 0:
            print("Por su compra tuvo un descuento del 12%!")
            new_total -= (new_total*0.12)
        return new_total

    def print_receipt(self, receipt_number, receipt, total):
        '''
            Imprime la factura del cliente y guarda un backup de la factura en base de datos
        '''
        print("-------------\nFactura: {:05d}\n-------------".format(receipt_number))
        food_receipt = []
        for food, info in receipt.items():
            print(">>Comida: {}\n>>Cantidad: {}\n>>Total: {}\n--------------".format(food, info["Cantidad"], info["Total"]))
            food_receipt.append(food)
        new_total = self.check_for_discount(total)
        print("El total de su compra es de {}$".format(new_total))
        self.allreceipts[receipt_number] = {"Comida":food_receipt, "Total":new_total}

    def print_backup(self):
        '''
            Imprime las facturas almacenadas mientras 
            el programa se ejecuto
        '''
        print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
        for receipt, info in self.allreceipts.items() :
            print("-- Factura: {:05d}\n--Comida: {}\n--Total: {}\n--------------".format(receipt, info["Comida"], info["Total"]))

    def execute(self):
        '''
            Ejecuta las funciones para atender al cliente
        '''
        receipt_number = 0
        continue_transaction = False
        while continue_transaction is False:
            print("Bienvenido a la Panaderia *Sin Nombre*!")
            new_receipt, new_total = self.get_products()
            self.print_receipt(receipt_number, new_receipt, new_total)
            option_valid = False
            while option_valid is False:
                option = input("Desea cerrar caja?: (Si o No): ").lower()
                if option == "no":
                    receipt_number += 1
                    option_valid = True
                    print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
                elif option == "si":
                    self.print_backup()
                    continue_transaction = True
                    option_valid = True
                else:
                    print("Esta opcion no es valida")


Bakery().execute()