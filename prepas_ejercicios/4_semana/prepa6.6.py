# Ejercicio 6.6: Escribir un programa que pregunte una fecha en 
# formato dd/mm/aaaa y muestre por pantalla la misma fecha en 
# formato dd de <mes> de aaaa donde <mes> es el nombre del mes.

database = {1:["Enero", 31], 2:["Febrero", 28], 3:["Marzo", 31], 4:["Abril", 30], 
            5:["Mayo", 31], 6:["Junio", 30], 7:["Julio", 31], 8:["Agosto", 31], 
            9:["Septiembre", 30], 10:["Octubre", 31], 11:["Noviembre", 30], 12:["Diciembre", 31]}

def get_date():
    valid = False
    while valid is False:
        try:
            date = input("Ingrese una fecha (dd/mm/aaaa):\n>> ")
            date = date.split("/")
            day, month, year = int(date[0]), int(date[1]), int(date[2])
            valid = True
        except ValueError:
            print("Por Favor escriba la fecha en formato (dd/mm/aaaa) usando solo numeros")
        except IndexError:
            print("Por Favor escriba la fecha en formato (dd/mm/aaaa)")
    return day, month, year

def check_date(day, month, year):
    if month in database:
        if day <= database[month][1]:
            print("La fecha ingresada es {} de {} del {}". format(day, database[month][0], year))
        else:
            print("El dia ingresado no concuerda con el calendario")
    else:
        print("El mes ingresado no concuerda con el calendario")

day, month, year = get_date()
check_date(day, month, year)