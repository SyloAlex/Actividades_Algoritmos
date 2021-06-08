from Competitor import Competitor
from Singer import Singer
from Musician import Musician
from Dancer import Dancer
from FreeStyle import FreeStyle

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

def register_singer():
    song = input("Ingrese el nombre de la cancion:\n>> ")
    author = input("Ingrese el autor de la cancion:\n>> ")

    return song, author

def register_dancer():
    style = input("Ingrese el nombre de la cancion:\n>> ")

    return style

def register_musician():
    while True:
        try:
            instrument_number = int(input("Ingrese el numero de instrumentos a tocar:\n>> "))
            break
        except:
            print("Ingrese la cantidad de instrumentos en numeros")
    instrument = []
    for x in range(instrument_number):
        instrument_name = input(f"Ingrese el nombre del intrumento #{x}:\n>> ")
        instrument.append(instrument_name)

    return instrument

def register_free_style():
    talent = input("Ingrese el talento a desempeñar:\n>> ")

    return talent

def register_competitor(competitors, competitor_number):
    name = input("Ingrese su nombre:\n>> ")
    while True:
        print("""
1. Solista
2. Grupo
        """)
        group_option = menu(2)
        if group_option == 1:
            group = "Solista"
        else:
            group = "Grupo"
        break
    while True:
        try:
            phone = int(input("Ingrese su numero telefonico (sin espacios o caracteres especiales):\n>> "))
            break
        except:
            print("ERROR: Ingrese un numero de telefono valido")
    print("""
1. Canto
2. Musica Instrumental
3. Baile
4. Free Style
    """)
    category_option = menu(4)
    if category_option == 1:
        category = "Canto"
        song, author = register_singer()
        competitor = Singer(name, group, category, phone, competitor_number, song, author)
        competitors.append(competitor)
    elif category_option == 2:
        category = "Musica Instrumental"
        instrument = register_musician()
        competitor = Musician(name, group, category, phone, competitor_number, instrument)
        competitors.append(competitor)
    elif category_option == 3:
        category = "Baile"
        style = register_dancer()
        competitor = Dancer(name, group, category, phone, competitor_number, style)
        competitors.append(competitor)
    else:
        category = "Free Style"
        talent = register_free_style()
        competitor = FreeStyle(name, group, category, phone, competitor_number, talent)
        competitors.append(competitor)

def show_competitors(competitors):
    if not competitors:
        print("Aun no se han registrado los competidores")
    else:
        print("\nParticipantes:\n")
        for competitor in competitors:
            competitor.print_attributes()
            print("-"*20)

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