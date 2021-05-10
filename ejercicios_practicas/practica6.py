# Ejercicio 1: Para una lista de variable X, genere una tupla cuyo segundo valor sea sqrt(x*2 - x)
import math

x = [1, 2, 3, 4, 5]

def tuple_of_x(num_list):
    y = [math.sqrt(number**2 - number) for number in num_list]
    num_tuple = list(zip(num_list, y))
    print(*num_tuple, sep="\n")

# tuple_of_x(x)

#Ejercicio 2: Simular una agenda que no permita tener dos reuniones a la misma hora

class Agenda:
    def __init__(self):
        self.schedule = set()
        self.agenda = []

    def get_meeting(self):
        valid = False
        while not valid:
            try:
                meeting = input("Ingresa la hora de la reunion: ")
                meeting = int(meeting)
                if meeting >= 0 and meeting <= 24:
                    valid = True
                else:
                    print("Puedes agendar reuniones entre las 0 y 24hrs")
            except ValueError:
                print("La hora de la reunion debe ser ingresada en numeros")
        return meeting
    
    def add_to_schedule(self, hour):
        self.schedule.add(hour)
        print(f"Se ha agendado tu reunion de las {hour}")
    
    def execute(self):
        print("Bienvenido a tu agenda personalizada!")
        valid = False
        while valid is False:
            hour = self.get_meeting()
            if hour not in self.schedule:
                reason = input("Cual es la reunion que deseas agendar?: ")
                self.add_to_schedule(hour)
                self.agenda.append(f">> Reunion a las {hour} sobre {reason}")
            else:
                print("No puedes tener dos reuniones a la misma hora")
            valid_option = False
            while valid_option is False:
                option = input("Deseas agendar una nueva reunion? (Si/No): ")
                if option.lower() == "no":
                    print("Entendido, su agenda quedo: ")
                    print(*self.agenda, sep="\n")
                    valid = True
                    valid_option = True
                elif option.lower() == "si":
                    print("Perfecto!")
                    valid_option = True
                else:
                    print("La opcion ingresada no es valida")

prueba = Agenda().execute()