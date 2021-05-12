# Ejercicio C7E1: Contar la cantidad de frutas en el diccionario cesta de frutas usando la lista
# frutas como referencia.

cesta = {"manzanas": 4, "naranjas": 19, "hamburguesas": 3, "sandwiches": 8}
frutas = ["manzanas", "naranjas", "peras", "parchitas", "uvas", "cambures"]

def fruit_quantity(fruit_dict, fruits):
    cantidad_de_frutas, cantidad_de_no_frutas = 0, 0
    for alimento, cantidad in fruit_dict.items():
        if alimento in fruits:
            cantidad_de_frutas += cantidad
        else:
            cantidad_de_no_frutas += cantidad
    print("Hay {} frutas en su cesta y {} objetos que no son frutas".format(cantidad_de_frutas, 
                                                                            cantidad_de_no_frutas))

fruit_quantity(cesta, frutas)