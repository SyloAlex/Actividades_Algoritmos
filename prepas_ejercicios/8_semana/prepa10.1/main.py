from functions import *

def main():
    print("\nBienvenido al Concurso de Talentos UNIMET\n")
    i = 0
    competitors = []
    valid = False
    while not valid:
        print("""
1. Registrar participante
2. Ver lista de oarticipantes
3. Salir
        """)
        option = menu(3)
        if option == 1:
            register_competitor(competitors, i)
            i += 1
        elif option == 2:
            show_competitors(competitors)
        else:
            print("El programa se cerrara.\nHasta pronto!")
            exit()
        valid = continue_menu()
    
main()