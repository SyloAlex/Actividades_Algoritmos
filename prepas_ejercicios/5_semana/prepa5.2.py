# Ejercicio 5.2: Una marca de joyería que realiza sus ventas a través de Instagram realizará un sorteo que 
# tendrá tres ganadores. Se sorteará la siguiente mercancía:
# Primer lugar: 1 collar, 2 pulseras, 2 pares de zarcillos y 3 anillos.
# Segundo lugar: 1 collar, 1 pulsera y 2 anillos.
# Tercer lugar: 1 pulsera y 1 par de zarcillos.
# Tu labor es diseñar para ellos un programa (con ayuda de la librería “random”) 
# que, de todos los usuarios que están participando (de máximo 30 caracteres, recibidos 
# como input y almacenados en una lista) seleccione a los 3 ganadores al azar e indique cuál fue el premio.

import random

def get_option():
    while True:
        try:
            option = int(input(">> "))
            if option == 1 or option == 2:
                break
            else:
                print("La opcion ingresada no es valida")
        except:
            print("Error: Debe ingresar una opcion numerica")
    
    return option

def register_user(database):
    user = input("Ingrese el usuario:\n>> ")
    if user not in database:
        database.append(user)
        print(f"Usuario @{user} registrado exitosamente")
    else:
        print("El usuario ya se encuentra registrado")
    
    return database

def check_database(database):
    flag = False
    if len(database) >= 3:
        flag = True
    
    return flag

def lottery(database):
    winner = []
    i = 1
    while i < 4:
        lottery_number = random.randint(0, len(database) - 1)
        if database[lottery_number] not in winner:
            winner.append(database[lottery_number])
            i += 1
    
    return winner

def print_winners(winners, prices):
    for index in range(len(winners)):
        print(f"{index + 1}er lugar: @{winners[index]} ha ganado {prices[index]}")

def continue_process():
    valid = False
    while not valid:
        response = input("Desea continuar?\n>> ").lower()
        if response == "si":
            event_continue = False
            valid = True
        elif response == "no":
            event_continue = True
            valid = valid = True
        else:
            print("La opcion ingresada no es valida")

    return event_continue

def main():
    database = []
    prices = ["1 collar, 2 pulseras, 2 pares de zarcillos y 3 anillos",
              "1 collar, 1 pulsera y 2 anillos",
              "1 pulsera y 1 par de zarcillos"]
    print("Bienvenidos al sorteo de joyeria")
    valid = False
    while not valid:
        print("Puede:\n1. Ingresar un usuario\n2. Realizar el sorteo")
        option = get_option()
        if option == 1:
            database = register_user(database)
        else:
            if check_database():
                winners = lottery(database)
                print_winners(winners, prices)
                exit()
            else:
                print("No hay suficientes usuarios para realizar el sorteo")
        valid = continue_process()

main()