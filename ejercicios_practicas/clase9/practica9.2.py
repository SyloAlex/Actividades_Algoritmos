# Ejercicio 3: Escriba una funcion que tome n argumentos,
# calcule su media y su desviacion estandar

def calculate_mean(*args):
    '''Calcula la media de los valores ingresados

    Returns:

    mean = {float}
    '''
    sumatory = 0
    num = 0
    for n in args:
        sumatory += n
        num +=1

    return sumatory/num

def calculate_deviation(*args):
    '''Calcula la desviacion de los valores ingresados

    Returns:

    mean = {float}
    '''
    mean = calculate_mean(*args)
    deviation = 0
    for number in args:
        deviation += (number-mean)**2
    result = (deviation/len(args))

    return result, mean

def main():
    value = range(100)
    mean, std = calculate_deviation(*value)
    print(f"Media>> {mean}\nDesviacion Estandar>> {std}")

if __name__ == "__main__":
    main()