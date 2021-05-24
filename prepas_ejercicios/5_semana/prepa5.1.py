# Ejercicio 5.1: Deseas crear un programa que te ayude a organizar 
# tus eventos y tareas

def get_options():
    '''
        Obtiene del usuario la opcion del menu.

        Input >> {int}
    '''
    valid = False
    while valid is False:
        try:
            option = int(input(">> "))
            valid = True
        except ValueError:
            print("Error: no introduzca letras o caracteres especiales")
    
    return option

def get_event_name():
    '''
        Obtiene del usuario el nombre del evento.

        Input >> {str}
    '''
    event_name = input("Ingrese el nombre del evento:\n>> ")

    return event_name

def get_hour():
    for hour in range(0, 25):
        print("- De {:02d}:00 a {:02d}:00".format(hour, hour + 1))
    valid = False
    while not valid:
        print("Ingrese la hora del evento (solo el primer numero):")
        option_hour = get_options()
        if option_hour >= 0 and option_hour <= 24:
            valid = True
        else:
            print("La opcion seleccionada no es valida")
    
    return option_hour

def get_month(months):
    print("Estos son los meses en su calendario:")
    for month_number, month in months.items():
        print("{}.- {}".format(month_number, month[0]))
    valid = False
    while not valid:
        print("Ingrese una de las opciones:")
        option_month = get_options()
        if option_month >= 1 and option_month <= 12:
            valid = True
        else:
            print("La opcion seleccionada no es valida")
    
    return option_month

def get_days(month_days, month_name):
    print("Estos son los dias en su calendario:")
    for day in range(1, month_days + 1):
        print(f">>{day} de {month_name}")
    valid = False
    while not valid:
        print("Ingrese el dia:")
        option_day = get_options()
        if option_day >= 1 and option_day <= month_days:
            valid = True
        else:
            print("La opcion seleccionada no es valida")
    
    return option_day

def get_event_date():
    months = {1: ["Enero", 31], 2: ["Febrero", 28], 3: ["Marzo", 31], 4: ["Abril", 30],
          5: ["Mayo", 31], 6: ["Junio", 30], 7: ["Julio", 31], 8: ["Agosto", 31],
          9: ["Septiembre", 30], 10: ["Octubre", 31], 11: ["Noviembre", 30],
          12: ["Diciembre", 31]}
    month = get_month(months)
    month_name = months.get(month)[0]
    month_days = months.get(month)[1]
    day = get_days(month_days, month_name)
    hour = get_hour()

    return month, day, hour

def check_event(calendar, month, day, hour, event):
    if calendar != {}:
        check_month = calendar.get(month, 0)
        if check_month == 0:
            calendar[month] = {day: {hour: event}}
            print("Se ha agregado exitosamente su evento 1")
        else:
            check_day = calendar[month].get(day, 0)
            if check_day == 0:
                calendar[month][day] = {hour: event}
                print("Se ha agregado exitosamente su evento 2")
            else:
                check_hour = calendar[month][day].get(hour, 0)
                if check_hour == 0:
                    calendar[month][day][hour] = event
                    print("Se ha agregado exitosamente su evento 3")
                else:
                    print("Ese horario ya esta ocupado")
    else:
        calendar[month] = {day: {hour: event}}
        print("Se ha agregado exitosamente su evento 4")

def continue_events():
    valid = False
    while not valid:
        response = input(">> ").lower()
        if response == "si":
            event_continue = False
            valid = True
        elif response == "no":
            event_continue = True
            valid = valid = True
        else:
            print("La opcion ingresada no es valida")

    return event_continue

def print_events(calendar):
    print("Estos son sus eventos en el calendario\n" + "-"*30)
    for month, month_info in calendar.items():
        for day, day_info in month_info.items():
            for hour, event in day_info.items():
                print(">>MES: {}\n>>DIA: {}\n>>HORA:{}\n>>EVENTO: {}".format(month, day, hour, event))
                print("-"*30)

def main():
    print("Bienvenido a tu calendario personal!")
    calendar = {}
    valid = False
    while not valid:
        event_name = get_event_name()
        month, day, hour = get_event_date()
        check_event(calendar, month, day, hour, event_name)
        print("Desea continuar agregando eventos?")
        valid = continue_events()
    print_events(calendar)

main()