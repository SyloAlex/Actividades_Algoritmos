import random
from Car import Car

def register_racer():
    while True:
        brand = input("Ingrese la marca del carro:\n>> ")
        driver = input("Ingrese el nombre del conductor:\n>> ")
        break
    racer = Car(brand, driver)
    
    return racer

def menu(max):
    while True:
        try:
            menu_option = int(input("Ingrese la opcion del menu:\n>> "))
            if menu_option >= 1 and menu_option <= max:
                break
            else:
                print("La opcion ingresada no es valida")
        except:
            print("Por favor solo ingrese numeros")
    
    return menu_option

def start_race(racers):
    i = 0
    positions = []
    while i < len(racers):
        position = random.randint(1, len(racers))
        if position not in positions:
            positions.append(position)
            racers[i].set_position(position)
            i += 1

def race_results(racers):
    racers.sort(key=lambda x: x.position)
    for racer in racers:
        print("""
Lugar: {}
Corredor: {}
        """.format(racer.position, racer.driver))


def show_database(racers):
    if racers == []:
        print("La base de datos esta vacia!")
    else:
        racers.sort(key=lambda x: x.driver)
        print("Base de Datos Carrera:")
        for racer in racers:
            print("""
    Nombre: {}
    Marca: {}
    -------------------""".format(racer.driver, racer.brand))

def continue_menu():
    valid = False
    while not valid:
        option_continue = input("Desea hacer algo mas? (Si o No):\n>> ").lower()
        if option_continue == "no":
            print("Entendido, que tenga un feliz dia!")
            return_valid = True
            valid = True
        elif option_continue == "si":
            return_valid = False
            valid = True
            continue
        else:
            print("La opcion ingresada no es valida, se retornara al menu!")
    
    return return_valid