# Desarrolle un programa que simule una carrera de 6 automóviles y el respectivo lugar de
# llegada de cada auto se verá dado aleatoriamente. Cada automóvil posee por lo menos
# dos características (atributos) que le permiten ser diferenciado con otros:

from Car import Car
from functions import *

def main():
    racers = []
    print("\nBienvenido al Colegio Santiago de Leon de Caracas:")
    valid = False
    while not valid:
        print("""
    Menu:
    1. Registrar conductor
    2. Iniciar carrera
    3. Ver base de datos
    4. Salir
        """)
        option = menu(4)
        if option == 1:
            if len(racers) < 6:
                racers.append(register_racer())
            else:
                print("Ya hay un maximo de competidores")
        elif option == 2:
            start_race(racers)
            race_results(racers)
        elif option == 3:
            show_database(racers)
        else:
            print("Hasta pronto!")
            exit()
        valid = continue_menu()
        if valid:
            racers = []

main()