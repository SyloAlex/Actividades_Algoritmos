# Ejercicio 5.3: Una nueva compañía de lotería te ha contratado para que diseñes un 
# programa que les permita:
# Generar los tickets para vender
# Seleccionar aleatoriamente uno de los tickets para que sea el ganador
# Cada ticket tiene 8 dígitos y debe poderse indicar por teclado la cantidad de tickets a generar.

import random

def get_ticket_quantity():
    '''
        Obtiene del usuario la cantidad de tickets
        a generar.

        Input >> {int}

        Returns:
        quantity = {int}
    '''
    while True:
        try:
            quantity = int(input("Ingrese la cantidad de tickets a generar:\n>> "))
            break
        except ValueError:
            print("Error: no introduzca letras o caracteres especiales")
    
    return quantity

def get_tickets(quantity, tickets):
    '''Obtener tickets random

    Arguments:
    quantity = {int}
    tickets = {list}

    Returns:
    tickets = {list} actualizada
    '''
    i = 1
    while i <= quantity:
        num = random.randint(0, 99999999)
        if num not in tickets:
            tickets.append(num)
            i += 1
    
    return tickets

def select_option():
    '''
        Obtiene del usuario la opcion del menu

        Input >> {int}

        Return:
        option = {int}
    '''
    while True:
        try:
            option = int(input("Ingrese la opcion:\n>> "))
            if option == 1 or option == 2:
                break
            else:
                print("La opcion seleccionada no es valida\n" + "-"*30)
        except ValueError:
            print("Error: no introduzca letras o caracteres especiales")
    
    return option

def select_winner(tickets):
    '''Selecciona al ganador al azar

    Arguments:
    tickets = {list}
    '''
    if tickets:
        winner_index = random.randint(0, len(tickets)-1)
        print(f"El ganador de la loteria es el ticket {tickets[winner_index]}")
    else:
        print("No se han generado tickets para el sorteo")

def continue_menu():
    '''Continuar o no en el menu

    Returns:
    continue_in_menu = {bool}
    '''
    valid = False
    while not valid:
        response = input("Desea continuar?\n>> ").lower()
        if response == "si":
            continue_in_menu = False
            valid = True
        elif response == "no":
            continue_in_menu = True
            valid = valid = True
        else:
            print("La opcion ingresada no es valida")

    return continue_in_menu

def main():
    '''Loteria

    Description: ejecuta las funciones para generar tickets
    y seleccionar al ganador
    '''
    print("Bienvenidos al equipo de loteria")
    tickets = []
    valid = False
    while not valid:
        print("1. Generar un ticket 2. Seleccionar al ganador")
        option = select_option()
        if option == 1:
            quantity = get_ticket_quantity()
            tickets = get_tickets(quantity, tickets)
            print(tickets)
        else:
            select_winner(tickets)
        valid = continue_menu()

main()