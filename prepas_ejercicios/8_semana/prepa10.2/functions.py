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