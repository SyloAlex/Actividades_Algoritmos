# Ejercicio 3.8: Realice un algoritmo que imprima por pantalla 
# la tabla de multiplicar del 1 al 10

def multiply_table():
    for table in range(1, 11):
        print(f"Tabla de multiplicar del {table}\n" + "-"*27)
        for number in range(1, 11):
            print("{} x {} = {}".format(table, number, table * number))
        print("\n" + ">"*27 + "\n")

multiply_table()