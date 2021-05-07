# Ejercicio 3.16: Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el
# usuario escriba “salir” que terminará el programa.

def eco():
    '''
        Repite lo que el usuario escriba hasta que su input sea salir
    '''
    print("Bienvenido a Eco. Si desea salir del programa, escriba 'salir'")
    valid = False
    while valid is False:
        inp = input("Escriba algo: ")
        print(inp)
        inp = inp.lower()
        if inp == 'salir':
            valid = True

eco()