# Una tienda te ha contratado para que programes una base de datos para
# llevar el registro de sus clientes. La base de datos debe contener lo
# siguiente:
# - Solicitar nombre, cedula y monto a cancelar
# - Llevar registro de las veces que un cliente realiza una compra
# - Si la suma de los ultimos tres numeros de la cedula del cliente es
# un numero oblongo se lo otorga un descuento del 7%
# - Por cada 5 veces que un mismo cliente vaya a la tienda se le dara un 10%
# de descuento.
# - Debe mostrarse un mensaje en la pantalla con monto sin descuento, 
# descuento aplicado y monto a pagar final
# - Debe tener todas las validaciones.

def menu_option(max):
    while True:
        try:
            option = int(input("Ingrese la opcion:\n>> "))
            if option >= 1 and option <= max:
                break
            else:
                print("La opcion ingresada no es valida")
        except:
            print("Error: La opcion ingresada no es un numero")
    
    return option

def menu_continue():
    flag = False
    while True:
        option = input("Desea continuar? (Si o No):\n>> ").lower()
        if option == "si":
            break
        elif option == "no":
            flag = True
            print("Adios!")
            break
        else:
            print("La opcion ingresada no es valida")
    
    return flag
    

def get_discount7(id):
    id_check = int(str(id)[-3:])
    discount7 = False
    for number in range(id_check):
        if number * (number + 1) == id_check:
            discount7 = True
            break
    
    return discount7

def get_discount10(db, id):
    flag = False
    for clients in db:
        for key, value in clients.items():
            if key == "Cedula":
                if value == id:
                    print(len(clients["Factura"]))
                    if (len(clients["Factura"]) + 1) % 5 == 0:
                        flag = True
    
    return flag

def check_client(db, id, cost, day, month, discount7, discount10):
    flag = False
    for clients in db:
        for key, value in clients.items():
            if key == "Cedula":
                if value == id:
                    clients["Factura"].append({str(day)+"/"+str(month): cost, "Descuento7": discount7, 
                                               "Descuento10": discount10})
                    flag = True
    return flag


def register_client(db):
    name = input("Ingrese el nombre y apellido del cliente:\n>> ")
    while True:
        try:
            id = int(input("Ingrese la cedula del cliente:\n>> "))
            cost = float(input("Ingrese el monto a cancelar: "))
            break
        except:
            print("Error: introduzca la cifra en numeros")
    while True:
        try:
            month = int(input("Ingrese el mes:\n>> "))
            if month >= 1 and month <= 12:
                break
            else:
                print("Los meses solo van del 1 al 12")
        except:
            print("Error: introduzca el mes en numeros")
    month31 = [1, 3, 5, 7, 8, 10, 12]
    month30 = [4, 6, 9, 11]
    while True:
        try:
            day = int(input("Ingrese el dia:\n>> "))
            if month in month31:
                if day >= 1 and day <= 31:
                    break
                else:
                    print("El dia no corresponde al mes ingresado")
            elif month in month30:
                if day >= 1 and day <= 30:
                    break
                else:
                    print("El dia no corresponde al mes ingresado")
            else:
                if day >= 1 and day <= 28:
                    break
                else:
                    print("El dia no corresponde al mes ingresado")
        except:
            print("Error: introduzca el dia en numeros")
    discount7 = get_discount7(id)
    discount10 = get_discount10(db, id)
    print("El cliente {} de cedula {} ha realizado una compra por {}".format(name, id, cost))
    if discount7:
        cost *= 0.93
        print(f"Obtuvo un descuento del 7% por su compra\nPor un total de {cost}")
    if discount10:
        cost *= 0.90
        print(f"Obtuvo un descuento del 10% por su compra\nPor un total de {cost}")
    check = check_client(db, id, cost, day, month, discount7, discount10)
    if not check:
        client = {}
        client["Nombre"] = name
        client["Cedula"] = id
        client["Factura"] = [{str(day)+"/"+str(month): cost, "Descuento7": discount7, 
                              "Descuento10": discount10}]
        db.append(client)

def print_database(db):
    print("Base de datos:\n" + "-"*30)
    for client in db:
        for key, value in client.items():
            if key != "Factura":
                print("{}: {}".format(key, value))
            else:
                print("Facturas:")
                for values in value:
                    for key2, value2 in values.items():
                        if key2 != "Descuento7" and key2 != "Descuento10":
                            print("Fecha: {} Monto: {}$". format(key2, value2))
                        else:
                            discount = "No aplica"
                            if value2 == True:
                                discount = "Si aplica"
                            print(">>{}: {}". format(key2, discount))
        print("-"*30)

def main():
    database = [
        {
            "Nombre": "Alex",
            "Cedula": 20616375,
            "Factura":[
                {
                    "25/5/21":100.0,
                    "Descuento7": False,
                    "Descuento10": False
                }
            ]
        },
        {
            "Nombre": "Sabry",
            "Cedula": 23612195,
            "Factura":[
                {
                    "28/5/21": 50.0,
                    "Descuento7": False,
                    "Descuento10": False
                },
                {
                    "29/5/21": 60.0,
                    "Descuento7": False,
                    "Descuento10": False
                }
            ]
        }
    ]
    print("Bienvenidos al sistema de facturacion!")
    valid = False
    while not valid:
        print("""
Puede:
1. Ingresar un cliente con su factura
2. Imprimir la base de datos
3. Salir
        """)
        option = menu_option(3)
        if option == 1:
            register_client(database)
        elif option == 2:
            print_database(database)
        else:
            print("Adios!")
            exit()
        valid = menu_continue()
        
main()