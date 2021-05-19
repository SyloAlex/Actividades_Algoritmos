# Ejercicio 6.7: Escribir un programa que gestione las facturas 
# pendientes de cobro de una empresa. Las facturas se almacenarán 
# en un diccionario donde la clave de cada factura será el número de factura 
# y el valor el coste de la factura. El programa debe preguntar al usuario 
# si quiere añadir una nueva factura, pagar una existente o terminar. 
# Si desea añadir una nueva factura se preguntará por el número de factura y 
# su coste y se añadirá al diccionario. Si se desea pagar una factura se preguntará 
# por el número de factura y se eliminará del diccionario. Después de cada operación 
# el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la 
# cantidad pendiente de cobro.

class Check_In_Machine:
    def __init__(self):
        self.database = {}
        self.debt = 0
        self.pay = 0
    
    def get_receipt(self):
        valid = False
        while valid is False:
            try:
                receipt = int(input("Ingrese el numero de la factura:\n>> "))
                cost = int(input("Ingrese el costo de la factura:\n>> "))
                valid = True
            except ValueError:
                print("Por Favor ingrese los datos en numeros")
        self.database[receipt] = cost
        self.debt += cost
        print("Su deuda actual es de {}$. Ha pagado {}$ hasta los momentos".format(self.debt, self.pay))
    
    def pay_receipt(self):
        valid = False
        while valid is False:
            try:
                pay_receipt = int(input("Ingrese el numero de la factura:\n>> "))
                valid = True
            except ValueError:
                print("Por Favor ingrese los datos en numeros")
        if pay_receipt in self.database:
            self.pay += self.database[pay_receipt]
            self.debt -= self.database[pay_receipt]
            self.database.pop(pay_receipt)
            print("-----------\nSe ha pagado exitosamente la factura")
            print("Su deuda actual es de {}$. Ha pagado {}$ hasta los momentos".format(self.debt, self.pay))
        else:
            print("La factura ingresada no se encuentra en el sistema")
    
    def print_receipts(self):
        print("\nFacturas:\n-----------------")
        for receipt, cost in self.database.items():
            print("Factura {}: {}$".format(receipt, cost))

    def execute(self):
        print("Bienvenido a su Caja de Cobro Virtual!")
        shutdown = True
        while shutdown is True:
            valid = False
            while valid is False:
                try:
                    option = int(input("Ingrese su opcion:\n1. Añadir una factura\n2. Pagar una Facturar\n3. Ver Facturas\n4. Cerrar el programa\n>> "))
                    if option >= 1 and option <= 4:
                        valid = True
                    else:
                        print("La opcion seleccionada no es valida")
                except ValueError:
                    print("Debe ingresar una opcion numerica")
            if option == 1:
                self.get_receipt()
            elif option == 2:
                self.pay_receipt()
            elif option == 3:
                self.print_receipts()
            else:
                print("Perfecto, el programa se cerrara")
                shutdown = False
            continue_process = input("Desea continuar? (si o no)\n>> ").lower()
            if continue_process == "si":
                continue
            elif continue_process == "no":
                print("Perfecto, el programa se cerrara")
                shutdown = False
            else:
                print("La opcion ingresada no es valida, se retornara al menu de inicio")
            

Check_In_Machine().execute()