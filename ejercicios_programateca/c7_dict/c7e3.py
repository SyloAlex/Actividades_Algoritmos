# Ejercicio C7E3: Se le ha contratado en la compañía super-security para que cree un sistema de 
# autenticación de usuarios. Para esto deberá crear una función el cual acepte 3 
# parámetros, el usuario, clave (estos datos debera pedirlos por teclado) y un
# diccionario llamado db en donde se tiene la información de la compañía de quienes 
# tienen acceso al sistema, esta función deberá decir si el usuario tiene acceso o no.

def get_input():
    '''
    Recibe el usuario y contraseña para verificar si tiene acceso a la plataforma
    '''
    user_input = input("Por favor ingrese su usuario: ")
    password_input = input("Por favor, ingrese su contraseña: ")
    return user_input, password_input

def check_credentials(database):
    valid = False
    while valid is False:
        user, password = get_input()
        if user in database:
            if database[user] == password:
                print(f"Autentificacion completada! Bienvenido {user}!")
                valid = True
            else:
                print("Contraseña invalida")
        else:
            print("Usuario invalido")

def main():
	db = {
			"benjamisharifker2001" : "1234",
			"kevinelpreparador" : "estudienp@lQuiz",
			"elsaman" : "unimet123"
	}
	check_credentials(db)
	
main()