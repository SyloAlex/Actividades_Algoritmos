from practica10_2 import menu, check_credentials, register, continue_menu

def main():
    '''Ejecuta super-security

    Descript: funcion que permite logear o registrarse en la plataforma
    super-security.
    '''
    db = {"benjamisharifker2001" : {"Contrasena": "1234p", "Edad": 70, "Email": "benjamin@unimet.com"}, 
          "kevinelpreparador" : {"Contrasena": "estudienp@lQuiz1", "Edad": 20, "Email": "kevin@unimet.com"}, 
          "elsaman" : {"Contrasena": "unimet123", "Edad": 24, "Email": "elsaman@unimet.com"}
          }
    print("Bienvenido a la base de datos UNIMET\nEste es el menu:")
    valid = False
    while not valid:
        option = menu()
        if option == 1:
            check_credentials(db)
        else:
            db = register(db)
        valid = continue_menu()
        
main()