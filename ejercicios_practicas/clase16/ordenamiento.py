import time
import random
#Ejercicio 1: Modifique el Algoritmo de Ordenamiento Insertion
#para ordenar cualquier tipo de dato

def insertion_sort(vector, compare=lambda x,y: x < y):
    for i in range(1, len(vector)):
        temp = vector[i]
        j = i - 1
        while j >= 0 and compare(temp, vector[j]):
            vector[j + 1] = vector[j]
            j -= 1
        vector[j + 1] = temp

    return vector

#Ejercicio 2: Mida los tiempos que se tardan los algoritmos de
#insercion, seleccion y mezcla en ordenar un vector de
#10.000 posiciones

array = []
for i in range(100):
    while True:
        number = random.randint(0, 100)
        if number not in array:
            array.append(number)
            break

start = time.time()
insertion_sort(array)
end = time.time()
print(end-start)
