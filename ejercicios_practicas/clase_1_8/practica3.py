#Ejercicios de practica para la clase de Tipos de datos, Operadores y Variables
from datetime import datetime

#Ejercicio 1. Cree un programa que pida al usuario su nombre y su edad. 
#Imprima un mensaje dirigido a ellos que les indique el año en que
#cumpliran 18 años.

class DataCollector:
    '''
        Recibe los datos del cliente y verifica que la edad escrita sea valida
    '''
    def __init__(self):
        self.name = ""
        self.age = 0
        date = datetime.today()
        self.year = date.year

    def get_input(self):
        self.name = input("Ingresa tu nombre y apellido aqui: ")
        valid = False
        while not valid:
            age = input("Ingresa tu edad aqui: ")
            try:
                age = int(age)
                if age < 0:
                    print("Tu edad no puede ser un numero negativo")
                if age == 0:
                    print("En serio un bebe recien nacido esta respondiendo",
                          "esto? Por favor escribe tu edad")
                if age > 0:
                    self.age = age
                    valid = True
            except ValueError:
                print("Por favor escribe tu edad en numeros, no con letras")
                continue

    def message(self):
        '''
            Realiza los calculos necesarios para saber cuando el usuario cumple o cumplio 18 años
        '''
        self.get_input()
        if self.age < 18:
            age_difference = 18 - self.age
            year_difference = self.year + age_difference
            print(f"{self.name}, cumpliras 18 años en {age_difference} años, probablemente",
                  f"entre el {year_difference-1} y el {year_difference}")
        if self.age == 18:
            print(f"{self.name}, como actualmente tienes 18 años, los cumpliste entre el 2020 y",
                  "2021. Feliz cumpleaños pandemico!")
        if self.age > 18:
            age_difference = self.age - 18
            year_difference = self.year - age_difference
            print(f"{self.name}, cumpliste 18 años hace {age_difference} años, probablemente",
                  f"entre el {year_difference-1} y el {year_difference}")

data = DataCollector().message()