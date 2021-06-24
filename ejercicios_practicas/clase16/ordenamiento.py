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

def merge(left, right):
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left
    result = []
    index_left = index_right = 0
    while len(result) < len(left) + len(right):
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1
        if index_right == len(right):
            result += left[index_left:]
            break
        if index_left == len(left):
            result += right[index_right:]
            break
    return result

def merge_sort(array):
    if len(array) < 2:
        return array

    midpoint = len(array) // 2
    return merge(
        left=merge_sort(array[:midpoint]),
        right=merge_sort(array[midpoint:]))

array = []
for i in range(10000):
    while True:
        number = random.randint(0, len(range(10000)) - 1)
        if number not in array:
            array.append(number)
            break

start = time.time()
print("Insertion>>", insertion_sort(array))
end = time.time()
print(end-start, "segundos")

start1 = time.time()
print("Merge>>", merge_sort(array))
end1 = time.time()
print(end1-start1, "segundos")
