# Ejercicio 4: Escriba una funcion que imprima un diccionario
# en la pantalla

def print_dictionary(**dictionary):
    for key, value in dictionary.items():
        print(f"{key.capitalize()}>> {value}")

def main():
    subject = {"Nombre": "Alex", "Edad": 28, "Cedula": 20616375, "Mascota": "Trino y Salem"}
    print_dictionary(**subject)

if __name__ == "__main__":
    main()