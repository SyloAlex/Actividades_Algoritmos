# Ejercicio 4.1A: El programa debe conseguir los valores de y correspondientes a los valores 
# de x dados en la siguiente lista: valores_x = [2,5,9,13] para f(x) = 2X (2 elevado a la x), 
# y almacenarlos en una lista de tuplas que deberá imprimirse posteriormente.

x_values = [2, 5, 9, 13]

def fx_function(values):
    fx = list(zip(values, (2**x for x in values)))
    print(fx)

fx_function(x_values)

# Ejercicio 4.14B: El programa debe tomar las coordenadas de la siguiente lista: 
# coord2 = [(4,1),(25,11),(8,5),(16,8),(45,77),(10,10),(4,1),(34,2),(25,11),(8,5)] 
# y mostrarlos de la siguiente forma, después de eliminar todos los puntos repetidos y 
# ordenar la lista de forma ascendente:

coord2 = [(4,1), (25,11), (8,5), (16,8), (45,77),
          (10,10), (4,1), (34,2), (25,11), (8,5)]

def sort_coords(coordinates):
    coords = sorted(set(coordinates))
    print("x    y\n------")
    for x, y in coords:
        print(f"{x}   {y}")

sort_coords(coord2)