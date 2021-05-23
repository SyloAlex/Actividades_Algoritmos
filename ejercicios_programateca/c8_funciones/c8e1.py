# Ejercicio 1: Escriba una función llamada densidad_de_poblacion que tome dos 
# argumentos: poblacion y area, y devuelva una densidad de población. 
# calculada a partir de esos valores.

def get_area_population():
    '''
        El usuario ingresa el area y la poblacion.

        Returns:
        area = {float}
        population = {int}
    '''
    valid = False
    while not valid:
        try:
            area = float(input("Ingrese el area (puede ser con decimales):\n>> "))
            if area < 0:
                print("El area no puede ser negativa")
            elif area == 0:
                print("El area no puede ser 0")
            else:
                valid = True
        except ValueError:
            print("El area solo puede ser numeros (con o sin decimales)")
    while valid:
        try:
            population = float(input("Ingrese la poblacion:\n>> "))
            if population < 0:
                print("La poblacion no puede ser negativa")
            elif population == 0:
                print("La poblacion no puede ser 0")
            else:
                valid = False
        except ValueError:
            print("La poblacion solo puede ser un numero entero")
    
    return area, population

def calculate_density(area, population):
    '''Calculo de densidad poblacional

    Arguments:
    area = {float} >> area del terreno
    population = {int} >> residentes en el area

    Returns:
    density = {float} >> densidad poblacional
    '''
    density = population / area

    return density

def main():
    area, population = get_area_population()
    density = calculate_density(area, population)
    print("La densidad poblacional es {:.2f}".format(density))

if __name__ == "__main__":
    main()