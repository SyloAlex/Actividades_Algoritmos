# Ejercicio 3.3: Con dos dados, al azar, se pueden obtener números entre 2 y 12 de varias formas. 
# Crea un programa que reciba por teclado un número entre 2 y 12 y retorne las combinaciones posibles 
# de números para que su suma sea igual al número ingresado (no debe repetirse la combinación, 
# por ejemplo, 4-5 y 5-4 debe mostrarse solo una vez).

class Dices:
    '''
        Calcula las distintas combinaciones que puede dar dos dados al lanzarlos, 
        el input es por parte del usuario
    '''
    def __init__(self):
        self.roll = 0

    def get_input(self):
        '''
            Obtiene del usuario la suma de ambos dados lanzados
        '''
        valid = False
        while valid is False:
            try:
                number = input("Por favor, escriba la suma de ambos dados: ")
                number = int(number)
                if number >= 2 and number <= 12:
                    valid = True
                    self.roll = number
                else:
                    print("El numero ingresado no es valido")
            except ValueError:
                print("La opcion seleccionada no es un numero")

    def dice_combination(self):
        '''
            Calcula todas las combinaciones segun el input
            del usuario
        '''
        self.get_input()
        combinations = []
        for num in range(1, 7):
            if (self.roll - num < 7):
                if [num, self.roll - num] not in combinations:
                    combinations.append([self.roll - num, num])
        print(combinations)

Dices().dice_combination()