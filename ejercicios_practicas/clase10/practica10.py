# Ejercicio 1.a: usar la funcion map() y funcion lambda para encontrar el promedio de
# cada vector en la matriz numbers.

numbers = [[34, 63, 88, 71, 29],
           [90, 78, 51, 27, 45],
           [63, 37, 85, 46, 22],
           [51, 22, 34, 11, 18]]

avg = list(map(lambda x: sum(x)/len(x), numbers))
print(avg)

# Ejercicio 1.b: Usar la funcion filter() para crear una lista con las ciudades con menos
# de 8 caracteres, tomando la lista ciudades como base.

citys = ["Caracas", "Margarita", "Maracaibo",
         "Barinas", "Puerto La Cruz", "Valencia"]

#small_citys = list(filter(lambda x: True if len(x) < 8 else False, citys))
small_citys = list(filter(lambda x: len(x) < 8, citys))
print(small_citys)