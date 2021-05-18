# Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono 
# y lo guarde en un diccionario. Después debe mostrar por pantalla la información

def get_basic_info():
    name = input("Cual es su primer nombre?\n>> ")
    last_name = input("Cual es su primer apellido?\n>> ")
    valid = False
    while valid is False:
        try:
            age = int(input("Cuantos años tiene?:\n>> "))
            phone_number = int(input("Cual es su numero telefonico? (Solo numeros):\n>> "))
            valid = True
        except ValueError:
            print("Por Favor escriba su edad y numero de telefono solo con numeros")
    address = input("Cual es su direccion?\n>> ")
    basic_info = {"Nombre": name, "Apellido": last_name, "Edad": age,
                  "Relefono": phone_number, "Direccion": address}
    print("----------------------------")
    for key, value in basic_info.items():
        print(">>", key, ":", value)

get_basic_info()