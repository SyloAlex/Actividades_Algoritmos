# Un colegio te ha contratado para que diseñes un programa que los ayude 
# a almacenar de una manera más sencilla toda la información de sus alumnos. 
# Cada alumno tiene nombre, grado que cursa, promedio, dirección de habitación, 
# nombre del representante, teléfono del representante y la condición de becado o no.

from Student import Student
from functions import *

def main():
    students = []
    print("\nBienvenido al Colegio Santiago de Leon de Caracas:")
    valid = False
    while not valid:
        print("""
    Menu:
    1. Registrar estudiante
    2. Estadisticas
    3. Ver base de datos
    4. Salir
        """)
        option = menu(4)
        if option == 1:
            students.append(register_student())
        elif option == 2:
            print("""
    Menu de Estadisticas:
    1. Top 5 del Colegio
    2. Promedio General
    3. Promedios < 10 y > 15
            """)
            statistics_option = menu(3)
            if statistics_option == 1:
                show_top_5(students)
            elif statistics_option == 2:
                general_mean(students)
            else:
                grade_ten_fifteen(students)
            pass
        elif option == 3:
            show_database(students)
        else:
            print("Hasta pronto!")
            exit()
        valid = continue_menu()

main()