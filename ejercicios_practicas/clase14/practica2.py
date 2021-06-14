# Escriba una funcion que genere numeros uniformes entre 0 y 1.
# Calcule Pi

import random

def number_generator(number):
    total_coord = 0
    circle_coord = 0
    for i in range(number):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        distance = (x ** 2) + (y ** 2)
        if distance < 1:
            circle_coord += 1
        total_coord += 1
    
    return 4 * (circle_coord / total_coord)

# print(number_generator(1000000))

def number_generator_2(number, total_coord = 0, circle_coord = 0):
    if number == 0:
        return 4 * (circle_coord / total_coord)

    x = random.uniform(0, 1)
    y = random.uniform(0, 1)
    distance = (x ** 2) + (y ** 2)
    if distance < 1:
        circle_coord += 1
    total_coord += 1
    number -= 1

    return number_generator_2(number, total_coord, circle_coord)

print(number_generator_2(997))