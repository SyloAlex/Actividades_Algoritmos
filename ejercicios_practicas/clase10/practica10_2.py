# Ejercicio 2: 
# Parte A: Se le ha contratado en la compañía super-security 
# para que cree un sistema de autenticación de usuarios. Para esto 
# deberá crear una función el cual acepte 3 parámetros, el usuario, 
# clave (estos datos debera pedirlos por teclado) y un diccionario 
# llamado db en donde se tiene la información de la compañía de quienes 
# tienen acceso al sistema, esta función deberá decir si el usuario tiene 
# acceso o no.
# Parte B: Crear un sign up que permite crear un usuario nuevo y pida
# usuario, contrasena, edad y correo (la contrasena debe tener al menos
# 1 letra y 1 numero)


def menu():
    '''Menu de la plataforma

    Inputs = {int}
    '''
    while True:
        try:
            option = int(input("1. Sign In\n2. Register\nIngrese la opcion\n>> "))
            if option == 1 or option == 2:
                break
            else:
                print("La opcion ingresada no es valida")
        except ValueError:
            print("Ingrese una opcion numerica")
    
    return option

def get_signin_data():
    '''
    Recibe el usuario y contraseña para verificar si tiene acceso a la plataforma
    '''
    user_input = input("Por favor ingrese su usuario: ")
    password_input = input("Por favor, ingrese su contraseña: ")
    return user_input, password_input

def check_credentials(database):
    '''Chequear en base de datos el usuario y contrasena

    Argument:
    database = {dict}
    '''
    print(database)
    valid = False
    while valid is False:
        user, password = get_signin_data()
        if database.get(user):
            if database[user]["Contrasena"] == password:
                print(f"Autentificacion completada! Bienvenido {user}!")
                valid = True
            else:
                print("Usuario o Contraseña invalido")
        else:
            print("Usuario o Contraseña invalido")

def register(database):
    '''Registro en la plataforma.

    Llama a las funciones get_password, get_email y get_age
    para guardar en el diccionario los datos

    Arguments:
    database = {dict}
    '''
    user = input("Ingrese su nuevo usuario:\n>> ")
    password = get_password()
    email = get_email()
    age = get_age()
    database[user] = {"Contrasena": password, "Edad": age, "Email": email}

    return database

def get_password():
    '''Obtiene la contrasena del usuario

    Input = {str}
    La contrasena se valida si tiene al menos 1 numero y 1 letra

    Return:
    password = {str}
    '''
    while True:
        password = input("Ingrese su contraseña:\n>> ")
        if len(password) > 8:
            num_check = list(filter(lambda character: character.isnumeric(), password))
            alpha_check = list(filter(lambda character: character.isalpha(), password))
            if num_check and alpha_check:
                break
            else:
                print("La contrasena debe contener al menos 1 letra y 1 numero")
        else:
            print("La contrasena debe ser mayor a 8 caracteres")
    
    return password

def get_email():
    '''Obtiene el email del usuario

    Input = {str}
    El email se valida si tiene @

    Return:
    email = {str}
    '''
    while True:
        email = input("Ingrese su correo:\n>> ")
        email_check = list(filter(lambda character: character == "@", email))
        if email_check:
            break
        else:
            print("Correo invalido")
    
    return email

def get_age():
    '''Obtiene la edad del usuario

    Input = {str}

    Return:
    age = {int}
    '''
    while True:
        try:
            age = int(input("Ingrese su edad:\n>> "))
            break
        except ValueError:
            print("Edad invalida: Use solo numeros")

    return age
    
def continue_menu():
    '''Continuar o salir de la plataforma

    Descript: funcion que valida si el usuario quiere realizar
    otro procedimiento en la plataforma o salir de la misma

    Input = {str}

    Return:
    flag = {boolean}
    '''
    while True:
        option = input("Desea continuar?\n>> ").lower()
        if option == "si":
            flag = False
            break
        elif option == "no":
            print("Entendido, se cerrara el programa")
            flag = True
            break
        else:
            print("La opcion seleccionada no es valida")
    
    return flag

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