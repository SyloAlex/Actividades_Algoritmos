# Ejercicio 2: Escriba una función llamada leer_tiempo().
# La función debe tomar un argumento, un número entero y 
# devolver un string que indique cuántas semanas y días son.

def get_time():
    '''
        El usuario ingresa un numero entero.

        Returns:
        time = {int}
    '''
    valid = False
    while not valid:
        try:
            time = int(input("Ingrese un numero entero:\n>> "))
            if time < 0:
                print("El numero no puede ser negativo")
            else:
                valid = True
        except ValueError:
            print("Por favor ingrese un numero entero positivo")

    return time

def calculate_week_day(time):
    '''Calcula los dias y semanas del numero ingresado

    Argument:
    time = {int} >> tiempo transcurrido

    Returns:
    week = {int} >> semanas transcurridas
    day = {int} >> dias transcurridos
    '''
    if time < 7:
        week = 0
        day = time
    else:
        week = time // 7
        day = time % 7
    
    return week, day

def main():
    time = get_time()
    week, day = calculate_week_day(time)
    print(f"El numero {time} corresponde a {week} semanas y {day} dias")

if __name__ == "__main__":
    main()