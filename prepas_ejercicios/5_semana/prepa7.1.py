# Ejercicio 7.3: Una cadena de comida rápida te necesita para la creación de un programa con 
# el que se pueda llevar una base de datos de los productos que ofrecen en su menú con su precio

menu = [
              ("Hamburguesas","Clásica", 4.00), ("Hamburguesas","Doble Carne", 4.80), 
              ("Hamburguesas","BBQ", 4.40), ("Hamburguesas","Pollo", 4.20), 
              ("Nuggets","15 piezas", 5.20), ("Nuggets","30 piezas", 9.50), 
              ("Papas fritas","Clásicas", 2.80), ("Papas fritas","Queso", 3.10), 
              ("Papas fritas","Queso y tocineta", 3.90), ("Helados","Vainilla", 1.30), 
              ("Helados","Fresa", 1.50), ("Helados","Chocolate", 1.50), ("Bebidas","Agua", 0.50), 
              ("Bebidas","Té","Limón", 1.10), ("Bebidas","Té","Durazno", 1.10), 
              ("Bebidas","Refresco","Coca-Cola", 0.90), ("Bebidas","Refresco","7-Up", 0.90), 
              ("Bebidas","Refresco","Freskolita", 0.90)
              ]

def convert_menu_to_dict(menu_list):
    '''
        Convierte la lista en un diccionario ordenado. menu_list = lista de comida con precios.
    '''
    menu_database = {}
    for food in menu_list:
        if len(food) == 3:
            if food[0] not in menu_database:
                menu_database[food[0]] = {food[1]: food[2]}
            else:
                menu_database[food[0]].update({food[1]: food[2]})
        else:
            if food[0] not in menu_database:
                menu_database[food[0]] = {food[1]: {food[2]: food[3]}}
            else:
                menu_database[food[0]].update({food[1]: {food[2]: food[3]}})

    return menu_database

def print_menu(menu_dict):
    print("Menu:")
    for food, info in menu_dict.items():
        print(f"--------\n{food}:")
        for food_type, price in info.items():
            if food_type == "Refresco" or food_type == "Té":
                for sub_type, real_price in price.items():
                    print(f"{food_type} >>> {sub_type} >>> {real_price}$")
            else:
                print(f"{food_type} >>> {price}$")
    print("----------------")

def get_high_low_price(menu_dict):
    high_price = ["", 0]
    low_price = ["", 0]
    for food, info in menu_dict.items():
        for food_type, price in info.items():
            if food_type == "Refresco" or food_type == "Té":
                for sub_type, real_price in price.items():
                    if real_price > high_price[1]:
                        high_price[0] = [food, food_type, sub_type]
                        high_price[1] = real_price
                    if low_price[1] == 0:
                        low_price[0] = [food, food_type, sub_type]
                        low_price[1] = real_price
                    else:
                        if low_price[1] > real_price:
                            low_price[0] = [food, food_type, sub_type]
                            low_price[1] = real_price
            else:
                if price > high_price[1]:
                    high_price[0] = [food, food_type]
                    high_price[1] = price
                if low_price[1] == 0:
                    low_price[0] = [food, food_type]
                    low_price[1] = price
                else:
                    if low_price[1] > price:
                        low_price[0] = [food, food_type]
                        low_price[1] = price

    return high_price, low_price

def print_low_high(high, low):
    if len(high[0]) == 3:
        print(f"El producto mas caro es {high[0][0]} {high[0][1]} de {high[0][2]} por el costo de {high[1]}")
    else:
        print(f"El producto mas caro es {high[0][0]} de {high[0][1]} por el costo de {high[1]}")
    if len(low[0]) == 3:
        print(f"El producto mas caro es {low[0][0]} {low[0][1]} de {low[0][2]} por el costo de {low[1]}")
    else:
        print(f"El producto mas caro es {low[0][0]} de {low[0][1]} por el costo de {low[1]}")


def execute(menu_list):
    new_menu = convert_menu_to_dict(menu_list)
    print("Bienvenido al Viejo McCaro!\n")
    print_menu(new_menu)
    high, low = get_high_low_price(new_menu)
    print_low_high(high, low)

execute(menu)